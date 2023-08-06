# -*- coding: utf-8 -*-
from numpy import sin, cos, pi, sqrt, exp, maximum, deg2rad, roll, mean
from pandas import read_csv, date_range, DataFrame
from pathlib import Path

file_path = Path(__file__).parent.parent # fixme: not suited for package upload


def read_PVGIS_TMY(path):
    """
    Extract from a PVGIS TMY *.csv file the relevant information to define a `Weather` instance.

    This corresponds to the attributes `external_temperature`, `direct_normal_irradiance` and `diffuse_horizontal_irradiance`
    of `Weather.__init__()`.

    Parameters
    ----------
    path: str or path-like
        Path of a TMY csv file downloaded from the PVGIS database [1]_.

    Returns
    -------
    df: pandas.DataFrame
        A (8760, 3) shaped DataFrame describing:

         * External temperature (°C) (column 'T2m' of CSV file at `path`).
         * Direct normal irradiance (kW/m2) (column 'I_b' of CSV file at `path`).
         * Diffuse horizontal irradiance (kW/m2) (column 'I_d' of CSV file at `path`).

    Notes
    -----
    1. Temperature data is given in Celsius degrees (°C), not in Kelvins (K).
    2. The 'G(h)' field from CSV file is the global horizontal irradiance.
       This column is not kept but calculated again using solar vector information.

    References
    ----------
    .. [1] Photovoltaic Geographical Information System, 2022. Online.
       Available from: https://re.jrc.ec.europa.eu/pvg_tools/fr/tools.html


    """
    df = read_csv(path, skiprows=16,
                  usecols=[1, 4, 5])
    df = df.iloc[:-10]
    df.rename({"T2m": "External temperature (°C)",
               "Gb(n)": "Direct normal irradiance (kW/m2)",
               "Gd(h)": "Diffuse horizontal irradiance (kW/m2)"},
              axis=1, inplace=True)
    df[["Direct normal irradiance (kW/m2)",
        "Diffuse horizontal irradiance (kW/m2)"]] /= 1e3
    df = df.astype(float)
    return df

def read_solar_vector(path):
    """
    Load a *.csv file describing the solar vector in an (azimuth, elevation) basis. These coordinates are needed to
    define a `Weather` instance.

    This corresponds to the attributes `azimuth` and `elevation` of `Weather.__init__()`.

    Parameters
    ----------
    path: str or path-like
       Path of a 3-columns csv file with:

        * first column: date-like or other field
        * second column: azimuth angle (eastward from North), in °.
        * third column: elevation angle, in °.

       The file must have a length of 8760 and a header row.

    Returns
    -------
    df: pandas.DataFrame
       A (8760, 2) shaped DataFrame describing:

        * alpha (°) (azimuth coordinate of CSV file at `path`).
        * gamma (°) (elevation coordinate of CSV file at `path`).

    Notes
    -----
    The Solar Position Algorithm (SPA) is a simple way to get the alpha and gamma coordinates for whatever location in the world. [1]_

    References
    ----------
    .. [1] AFSHIN ANDREAS. SPA Calculator. Online. NREL.
       Available from: https://midcdmz.nrel.gov/solpos/spa.htmlCompute the solar position from universal time
       and location using NREL’s Solar Position Algorithm (SPA).

    """
    df = read_csv(path, usecols=[2, 3])
    df.columns = ["alpha (°)", "gamma (°)"]
    return df

def get_weather(TMY_path, solar_vector_path, shift=0):
    """
    Define quickly a Weather instance by loading data from disk.

    Parameters
    ----------
    TMY_path:  str or path-like
        Path of a TMY csv file downloaded from the PVGIS database [1]_.

    solar_vector_path: str or path-like
        Path of a 3-columns csv file with:

        * first column: date-like or other field
        * second column: azimuth angle (eastward from North), in °.
        * third column: elevation angle, in °.

       The file must have a length of 8760 and a header row.

    shift: int, optional, default 0
        Time zone shift, negative west from Greenwich, in hours.
        All values (TMY, solar vector) are shifted of `shift` hours.

    Returns
    -------
    weather: Weather

    References
    ----------
    .. [1] Photovoltaic Geographical Information System, 2022. Online.
       Available from: https://re.jrc.ec.europa.eu/pvg_tools/fr/tools.html

    """
    """
    i) read typical meteorological year
    ==> this one comes from PVGIS: https://re.jrc.ec.europa.eu/pvg_tools/fr/
    """
    weather_data = read_PVGIS_TMY(TMY_path)
    weather_data = weather_data.values.T

    """
    ii) read solar vector
    ==> this one comes from https://midcdmz.nrel.gov/spa/
    """
    solar_vector = read_solar_vector(solar_vector_path)
    solar_vector = solar_vector.values.T

    # if local time is needed
    weather_data = roll(weather_data, shift, axis=1)
    solar_vector = roll(solar_vector, shift, axis=1)

    """
    iii) create a Weather object
    """
    weather = Weather(*weather_data, *solar_vector)

    return weather


class Weather:
    """
    A Weather instance is a container for meteorological (temperature, irradiance) and solar position (azimuth, elevation) data.

    Weather instances are required by `Demand` instances to compute space heating space cooling thermal demands.

    """
    # fixme: temperature in °C does not comply with other modules (weather, setpoint temp in class Demand)
    def __init__(self,
                 external_temperature,
                 direct_normal_irradiance,
                 diffuse_horizontal_irradiance,
                 azimuth,
                 elevation
                 ):
        """
        Creates Weather object and computes solar irradiance profiles required by Demand.

        Heating and cooling seasons are also defined.
        The cooling season is the longest period for which the mean weeekly temperature is above 12°C.
        The heating season is the complementary of the cooling season in the year.

        Parameters
        ----------
        external_temperature : list
            In °C. Length 8760.
            Hourly values of the ambient outdoor air temperature.
        direct_normal_irradiance : list
            In kW/m2. Length 8760.
            Hourly values of direct solar irradiance, on a perpendicular plane to sunrays.
        diffuse_horizontal_irradiance : list
            In kW/m2. Length 8760.
            Hourly values of diffuse solar irradiance.
        azimuth : list
            In °. Length 8760.
            The first coordinate of the solar vector.
            Reference is north, going eastward (clockwise).
        elevation : list
            In °. Length 8760.
            The second coordinate of the solar vector.

        """

        self._weather_data = DataFrame({"External temperature (°C)": external_temperature,
                                        "Direct normal irradiance (kW/m2)": direct_normal_irradiance,
                                        "Diffuse horizontal irradiance (kW/m2)": diffuse_horizontal_irradiance
                                        })
        # self.weather_data["Diffuse horizontal irradiance (kW/m2)"] *= 1/3
        self._solar_vector = DataFrame({"alpha (°)": azimuth,
                                        "gamma (°)": elevation})
        self.__add_heating_season()
        self.__add_solar_vector_cartesian_coordinates()
        self.__add_cartesian_irradiance()

    @property
    def weather_data(self):
        """
        A DataFrame containing the data read from disk and computed.

        """
        return self._weather_data

    @property
    def season_length(self):
        """
        The lengths of heating ('HS') and non heating seasons ('NHS'), in hours.

        """

        return self._season_length

    def __add_solar_vector_cartesian_coordinates(self):
        self._solar_vector["East"] = sin(deg2rad(self._solar_vector["alpha (°)"])) \
                                     * cos(deg2rad(self._solar_vector["gamma (°)"]))
        self._solar_vector["North"] = cos(deg2rad(self._solar_vector["alpha (°)"])) \
                                      * cos(deg2rad(self._solar_vector["gamma (°)"]))
        self._solar_vector["Horizontal"] = sin(deg2rad(self._solar_vector["gamma (°)"]))

    def __add_cartesian_irradiance(self):
        self.add_custom_irradiance(0, 0, 1, "horizontal")
        self.add_custom_irradiance(1, 0, 0, "east")
        self.add_custom_irradiance(0, -1, 0, "south")
        self.add_custom_irradiance(-1, 0, 0, "west")
        self.add_custom_irradiance(0, 1, 0, "north")

    def add_custom_irradiance(self, east, north, horizontal, name):
        """
        Compute the global irradiance (kW/m2) received by a surface described by the coordinates of its normal vector.

        Based on the scalar product of the solar vector coordinates and the surface vector coordinates.

        Parameters
        ----------
        east : float
            0 <= east <= 1
            East coordinate of the normal vector.
        north : float
            0 <= north <= 1
            North coordinate of the normal vector.
        horizontal : float
            0 <= horizontal <= 1
            Horizontal coordinate of the normal vector.
        name : str
            Custom name to identify the created data in `weather_data` attribute.
            Full name is "Global `name` irradiance (kW/m2)".


        Returns
        -------
        values : numpy.ndarray
            The calculated values.

        """
        name = str(name)
        try:
            0 <= east <= 1
            0 <= north <= 1
            0 <= horizontal <= 1
        except Exception as e:
            raise AttributeError(f"{self}: Incorrect values for 'east', 'north' or 'horizontal'.")
        diffuse = self.weather_data["Diffuse horizontal irradiance (kW/m2)"]
        direct = self.weather_data["Direct normal irradiance (kW/m2)"]
        self.weather_data[f"Global {name} irradiance (kW/m2)"] = direct * maximum(east * self._solar_vector["East"]
                                                                                  + north * self._solar_vector["North"]
                                                                                  + horizontal * self._solar_vector[
                                                                                      "Horizontal"],
                                                                                  0) \
                                                                 + diffuse
        return self.weather_data[f"Global {name} irradiance (kW/m2)"].to_numpy()

    def add_soil_temperature(self,
                             alpha=2.42 / (3200 * 840),
                             depth=1):
        """
        Compute the soil temperature at a given depth, according to the model of (Kusuda et al., 1965) [1]_.

        Parameters
        ----------
        alpha : float
            In m2/s.
            Thermal diffusivity of the soil.
        depth :  float
            depth > 0. In m.
            Depth for calculation of the soil temperature.

        Notes
        -----
        This method adds a column 'Soil temperature - `x`m depth (°C)' to attribute `weather_data`, with `x` a one-decimal rounding of `depth`.

        References
        ----------
        .. [1]  KUSUDA, T and ACHENBACH, P.R., 1965.
           Earth temperature and thermal diffusivity at selected stations in the United States. June 1965. P.236.


        """
        """
        Unused here. Computes underground temperature of the soil at a given depth.
        :param alpha: [float] Thermal diffusivity of the soil (in m²/s).
        :param depth: [float] (in m)
        :return: None. Data is added to weather_data DataFame.
        """
        # from T. Kusuda and P.R. Archenbach
        self.weather_data.set_index(date_range("01/01/2019", freq="h", periods=8760), inplace=True)
        T_mean_annual = mean(self.weather_data["External temperature (°C)"].to_numpy())         # faster than pd.DataFrame.mean
        DT_mean_daily = mean(self.weather_data.groupby(self.weather_data.index.dayofyear)["External temperature (°C)"] \
            .agg([lambda x_: -min(x_), max]).sum(axis=1).to_numpy())
        alpha *= 24 * 3600  # unit conversion: m²/day
        x = sqrt(pi / (365 * alpha))
        current_day = self.weather_data.index.dayofyear
        day_shift = self.weather_data.groupby(self.weather_data.index.dayofyear)["External temperature (°C)"]\
            .mean().idxmin()
        self.weather_data["Soil temperature - {:.1f}m depth (°C)".format(depth)] = \
            T_mean_annual - DT_mean_daily * exp(-depth * x) * cos(
                (2 * pi / 365) * (current_day - day_shift - (depth / 2) * x))
        self._weather_data = self.weather_data.reset_index(drop=True)

    def __add_heating_season(self):
        nu_b = 12
        df = self.weather_data

        # mean temperature is (min+max)/2
        df_weekly = df["External temperature (°C)"].groupby((df.index // (7 * 24))).agg([lambda x: min(x), max]).mean(
            axis=1)
        nbr_weeks = len(df_weekly)
        # heating season (HS): when the weekly temperature is below daily_temp_threshold
        # necessary 'while' to respect continuity property of heating season
        assumed_NHS_week = df_weekly.idxmax()

        last_possible_heating_week = assumed_NHS_week
        while df_weekly.loc[last_possible_heating_week] >= nu_b:
            last_possible_heating_week = (last_possible_heating_week - 1) % nbr_weeks

        first_possible_heating_week = assumed_NHS_week
        while df_weekly.loc[first_possible_heating_week] >= nu_b:
            first_possible_heating_week = (first_possible_heating_week + 1) % nbr_weeks

        if first_possible_heating_week >= last_possible_heating_week:
            # Northern part of the globe, winter is spread among 2 years
            df["Season"] = "NHS"
            df["Season"].where(
                (df.index // (7 * 24)).isin(range(last_possible_heating_week + 1, first_possible_heating_week)),
                "HS", inplace=True)
        else:
            # Southern part of the globe, winter is spread among 1 year
            df["Season"] = "HS"
            df["Season"].where(
                (df.index // (7 * 24)).isin(range(first_possible_heating_week, last_possible_heating_week + 1)),
                "NHS", inplace=True)

        self._weather_data = df.reset_index(drop=True)
        self._season_length = {"HS": len(self.weather_data[self.weather_data["Season"] == "HS"]),
                               "NHS": len(self.weather_data[self.weather_data["Season"] == "NHS"])}

