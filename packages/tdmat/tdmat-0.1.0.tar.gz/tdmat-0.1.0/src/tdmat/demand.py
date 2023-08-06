from importlib.resources import path as path_resources
from numpy import isnan, exp, log, array
from pandas import read_csv
from pathlib import Path
from zipfile import ZipFile

import tdmat._data.Tabula as Tabula_data
import tdmat._data.DHW_sizing as DHW_sizing_data

class Building:
    """
    Container for properties of a building of the Tabula database.

    """
    with path_resources(Tabula_data, 'Tabula.zip') as f:
        archive = ZipFile(f)
        content_TD1 = archive.open("Calc_Building_Set.csv","r")
        _TD1 = read_csv(content_TD1, skiprows=[1, 2, 3, 4, 5, 6, 7, 8, 9], index_col=0, encoding="latin1")
        content_TD2 = archive.open("Tab_Building.csv","r")
        _TD2 = read_csv(content_TD2, skiprows=[1, 2, 3, 4, 5, 6, 7, 8, 9], index_col=0, encoding="latin1")

    buildings_list = list(_TD1.index.unique().dropna())[2:]

    def __init__(self, name):
        """
        Read construction and thermal information of a given building of the Tabula database.

        Parameters
        ----------
        name : str
            Complete building variant name of a building from the Tabula database.

        Notes
        -----
        1. A list gathering approximately the names of the buildings of the Tabula database is stored in the `buildings_list` class attribute.
           One can also access the following link to navigate a user-friendly interface presenting Tabula buildings:
           https://webtool.building-typology.eu/#bm
        2. Properties are read from tabs 'Calc_Building_Set' and 'Tab_Building' of the Tabula master file.
           (discussed in https://episcope.eu/communication/download/)
           These tabs are stored as pandas.DataFrame as private attributes of `Building`, named _TD1 and _TD2.
        3. Additional properties are calculated on top of the one read from the Tabula Database. These are:

           * Typical DHW water storage mass for a building of that size.
             This is stored in the `DHW_storage_mass` attribute, in kg/m2.
             DHW_storage_mass =  (15.5 * n_Apartment + 156) / A_C_Ref
             It is derived from data of (Braas et al., 2020) [2]_.
           * An estimation of the roof area available for an installation of solar panels.
             This is stored in the `roof_solar_area` attribute, in m2/m2.
             The calculation does not rely on validated scientific hypothesis.
             It is assumed this area is half the total roof area available
             roof_solar_area = 0.5 * (A_Roof_1 + A_Roof_2) / A_C_Ref


        References
        ----------
        .. [2] BRAAS, Hagen, JORDAN, Ulrike, BEST, Isabelle, OROZALIEV, Janybek and VAJEN, Klaus, 2020.
           District heating load profiles for domestic hot water preparation with realistic simultaneity using DHWcalc and TRNSYS.
           Energy. 15 June 2020. Vol. 201, p. 117552. DOI 10.1016/j.energy.2020.117552.

        Examples
        --------
        >>> building = Building("ES.ME.MFH.02.Gen.ReEx.001.003")

        """
        self.name = name
        self.__read_parameters()
        self.__compute_basic_properties()

    @classmethod
    def _get_TD(cls, TD_num, name, col):
        assert TD_num in [1, 2]
        TD = cls._TD1 if TD_num == 1 else cls._TD2
        res = TD.loc[name, col]
        if isinstance(res, str):
            return float(res)
        elif isnan(res):
            return 0
        else:
            return res

    def __read_parameters(self):
        for parameter in ["A_C_Ref", "F_sh_hor", "F_sh_vert", "F_f", "F_w", "g_gl_n", "phi_int", "a_H"]:
            value = self._get_TD(1, self.name, parameter)
            setattr(self, parameter, value)

        for parameter in ["A_Roof_1", "A_Roof_2", "n_Apartment"]:
            value = self._get_TD(2, self.name[:-4], parameter)
            setattr(self, parameter, value)

        self.A_Window = {}
        for orient in ["Horizontal", "East", "South", "West", "North"]:
            self.A_Window[orient] = self._get_TD(1, self.name, f"A_Window_{orient}")

        self.h_ht = (self._get_TD(1, self.name, "h_Transmission") + self._get_TD(1, self.name, "h_Ventilation")) \
                    * self._get_TD(1, self.name, "F_red_temp")

    def __compute_basic_properties(self):
        self.DHW_storage_mass: "kg/m2" = (15.5 * self.n_Apartment + 156) / self.A_C_Ref
        self.roof_solar_area: "m2/m2" = 0.5 * (self.A_Roof_1 + self.A_Roof_2) \
                                        / self.A_C_Ref

    def __repr__(self):
        return f"{self.name}:\n" + \
               f"- area: {self.A_C_Ref} m²\n" + \
               f"- h_ht: {self.h_ht:.2f} W/(K.m²)\n" + \
               f"- DHW_storage_mass: {self.DHW_storage_mass:.2f} kg/m²\n" + \
               f"- roof_solar_area: {self.roof_solar_area:.2f} m²/m²\n"


class Demand:
    """
    Demand instances associate a Weather and a Building instance to define space heating (SH), space cooling (SC) and DHW thermal
    demands (DHW) of a Tabula building.

    These thermal demands are stored in attribute `df` while

    """

    def __init__(self, building, weather,
                 DHW_profile_draw_off,
                 DHW_proportions={"draw-off": 0.6, "circulation": 0.4},
                 E_DHW=20000,
                 nu_SH=lambda T_air: 20,
                 nu_SC=lambda T_air: max(22, T_air - 7),
                 drop_contributions=True
                 ):
        """
        Create the Demand instance and define all three thermal demands: SH, SC and DHW.

        DHW is also described by the maximum power demand that the DHW production system at building scale must be able
        to meet. This is a peak demand that may arise, it must be distinguished from `DHW_profile_draw_off`, which is the regular demand.

        Parameters
        ----------
        building : Building
            The buildings those thermal demands are calculated.
        weather : Weather
            The weather conditions at the location of `building`.
        DHW_profile_draw_off : numpy.ndarray
            Length 8760. Arbitrary unit, energy or volume.
            The time series profile of DHW draw-off.
            Draw-off of DHW corresponds to real use of DHW, contrary to recirculation DHW demand.
        DHW_proportions : dict {"draw-off": float, "circulation": float}
            Each value of `DHW_proportions` lies in [0,1], with the sum of the two values being 1.
            Describes the shares of `E_DHW` dedicated to the real energy DHW demand ('draw-off') and to the circulation
            part ('circulation').
            The time series profile of the circulation part is flat, i.e. at every moment the energy demand for circulating DHW
            is constant.
        E_DHW : float
            In Wh/m2.
            Annual total energy DHW demand (draw-off + circulation).
        nu_SH : callable f(x), optional, default lambda x: 20
            The function of the ambient outdoor air temperature (x, in °C) that gives the indoor setpoint temperature for SH demand.
        nu_SC : callable f(x), optional, default lambda x: max(22, x-7)
            The function of the ambient outdoor air temperature (x, in °C) that gives the indoor setpoint temperature for SC demand.
        drop_contributions : bool, optional, default True
            Whether the physical data calculated to determine thermal demands is dropped from the main attribute `df`.

        """
        self.E_DHW = E_DHW
        self.nu_SH = nu_SH
        self.nu_SC = nu_SC
        self.DHW_proportions = DHW_proportions
        self.DHW_profile_draw_off = array(DHW_profile_draw_off)
        self.building = building
        self.weather = weather
        self.df = self.weather.weather_data.copy()
        self.set_DHW_sizing_parameters(15)
        self.__compute_load(drop_contributions)

    @classmethod
    def set_DHW_sizing_parameters(cls, DHW_sizing_time_step):
        """
        Set the time step that define the maximum annual DHW power demand.

        This parameter is used to define the `DHW_sizing_power` (kW/m2) attribute.

        Parameters
        ----------
        DHW_sizing_time_step: {3, 15}
            In minutes.
            Qualifies the time step of the energy simulation ran using the DHWCalc tool [3]_.

        Notes
        -----
            1. This method is called at instance creation with `DHW_sizing_time_step`=15.
            2. Setting `DHW_sizing_time_step` = 3 leads to higher maximum demand due to a smaller simultaneity factor in DHW draw-offs.
            3. Energy simulation using DHWCalc lead to the following experimental log relations:

               * for `DHW_sizing_time_step` = 15:
                 exp(-(0.8903 * log(min(n_Apartment, 200)) + 3.0937))
               * for `DHW_sizing_time_step` = 3:
                 exp(-(0.9998 * log(min(n_Apartment, 200)) + 1.8547))

            4. The changes involved by setting `DHW_sizing_time_step` are common to all `Demand` instances.

        References
        ----------
        .. [3] JORDAN, Ulrike, VAJEN, Klaus and KASSEL, Universität, 2005.
           DHWcalc: PROGRAM TO GENERATE DOMESTIC HOT WATER PROFILES WITH STATISTICAL MEANS FOR USER DEFINED CONDITIONS.
           ISES Solar World Congress, Orlando (US). 12 August 2005. P. 6.

        """
        assert DHW_sizing_time_step in [3, 15]
        cls._DHW_sizing_time_step = DHW_sizing_time_step
        with path_resources(DHW_sizing_data, fr'Peak power - {cls._DHW_sizing_time_step} min.csv') as f:
            cls._DHW_sizing_discrete_values = read_csv(f, index_col=0)
        if DHW_sizing_time_step == 15:
            cls.DHW_sizing_continuous_function = lambda n_Apartment: exp(
                -(0.8903 * log(min(n_Apartment, 200)) + 3.0937))
        else:
            cls.DHW_sizing_continuous_function = lambda n_Apartment: exp(
                -(0.9998 * log(min(n_Apartment, 200)) + 1.8547))

    @classmethod
    def get_DHW_sizing_power(cls, n_Apartment):

        """
        Returns the annual maximum DHW power demand that may exist in a building having `n_Apartment`.

        Used to define

        Related to the `set_DHW_sizing_parameters` method.

        Parameters
        ----------
        n_Apartment : int
            The number of appartments of the building.

        Returns
        -------
        The maximum DHW power demand depending on the annual draw-off DHW energy demand.
        In kW / kWh.

        * For small number of apartments (<=50), real simulation values are used.
        * For n_Apartments in values = [1 -> 50] U [50, 60, 70, 80, 90, 100, 200], discrete values are used.
        * Else, the log fitting described in the documentation of `set_DHW_sizing_parameters` is used.

        Notes
        -----
        This power is calculated using annual energy simulation of DHW demand for various number of apartments
        using the DHWCalc tool [1]_.

        References
        ----------
        .. [1] JORDAN, Ulrike, VAJEN, Klaus and KASSEL, Universität, 2005.
           DHWcalc: PROGRAM TO GENERATE DOMESTIC HOT WATER PROFILES WITH STATISTICAL MEANS FOR USER DEFINED CONDITIONS.
           ISES Solar World Congress, Orlando (US). 12 August 2005. P. 6.


        """
        n_Apartment = int(n_Apartment)
        if (n_Apartment in cls._DHW_sizing_discrete_values.index) and (n_Apartment != 1000):
            return cls._DHW_sizing_discrete_values.loc[n_Apartment, "Peak power (kW/kWh)"]
        else:
            print(
                f"DHW sizing: No entry for n_Apartment={n_Apartment} "
                f"in file 'Peak power - {cls._DHW_sizing_time_step} min.csv',"
                f"\nusing log fitting instead.")
            return cls.DHW_sizing_continuous_function(n_Apartment)

    def __compute_solar_gains(self):
        self.df["Solar gains (W/m2)"] = 0
        for orient in ["Horizontal", "East", "South", "West", "North"]:
            F_SH = self.building.F_sh_hor if orient == "Horizontal" else self.building.F_sh_vert
            self.df["Solar gains (W/m2)"] += F_SH \
                                             * self.building.A_Window[orient] \
                                             * self.df[f"Global {orient.lower()} irradiance (kW/m2)"]

        self.df["Solar gains (W/m2)"] *= 1e3 \
                                         * (1 - self.building.F_f) \
                                         * self.building.F_w \
                                         * self.building.g_gl_n \
                                         / self.building.A_C_Ref

    def __compute_internal_gains(self):
        self.df["Internal gains (W/m2)"] = self.building.phi_int

    def __compute_SH_demand(self):
        self.df["Heat transfer losses SH (W/m2)"] = self.building.h_ht * \
                                                    (self.df["External temperature (°C)"].apply(self.nu_SH)
                                                     - self.df["External temperature (°C)"])

        self.gamma_h_gn = self.df.loc[
                              self.df["Season"] == "HS", ["Solar gains (W/m2)", "Internal gains (W/m2)"]].sum().sum() \
                          / self.df.loc[self.df["Season"] == "HS", "Heat transfer losses SH (W/m2)"].sum()
        self.eta_h_gn = (1 - self.gamma_h_gn ** self.building.a_H) / (1 - self.gamma_h_gn ** (self.building.a_H + 1))

        self.df["SH"] = self.df["Heat transfer losses SH (W/m2)"] \
                        - self.eta_h_gn * (self.df["Solar gains (W/m2)"] + self.df["Internal gains (W/m2)"])

        # non zero values of 'effective' columns are the one that define a SH demand
        cond = (self.df["Season"] == "HS") & (self.df["SH"] > 0)

        self.df["Heat transfer losses SH effective (W/m2)"] = \
            self.df["Heat transfer losses SH (W/m2)"].where(cond, 0)

        self.df["Solar gains SH effective (W/m2)"] = \
            self.df["Solar gains (W/m2)"].where(cond, 0)

        self.df["Internal gains SH effective (W/m2)"] = \
            self.df["Internal gains (W/m2)"].where(cond, 0)

        self.df["SH"] = \
            self.df["SH"].where(cond, 0)

    def __compute_SC_demand(self):
        self.df["Heat transfer losses SC (W/m2)"] = self.building.h_ht * (self.df["External temperature (°C)"]
                                                                          - self.df["External temperature (°C)"].apply(
                    self.nu_SC))

        self.df["SC"] = self.df["Heat transfer losses SC (W/m2)"] \
                        + self.df["Solar gains (W/m2)"] \
                        + self.df["Internal gains (W/m2)"]

        # non zero values of 'effective' columns are the one that define a SC demand
        cond = (self.df["Season"] == "NHS") & (self.df["SC"] > 0)

        self.df["Heat transfer losses SC effective (W/m2)"] = \
            self.df["Heat transfer losses SC (W/m2)"].where(cond, 0)

        self.df["Solar gains SC effective (W/m2)"] = \
            self.df["Solar gains (W/m2)"].where(cond, 0)

        self.df["Internal gains SC effective (W/m2)"] = \
            self.df["Internal gains (W/m2)"].where(cond, 0)

        self.df["SC"] = \
            self.df["SC"].where(cond, 0)

    def __compute_DHW_demand(self):
        self.scaled_DHW_profile_draw_off = (self.E_DHW * self.DHW_proportions[
            "draw-off"] / self.DHW_profile_draw_off.sum()) * self.DHW_profile_draw_off
        self.scaled_DHW_profile_circ = self.E_DHW * self.DHW_proportions["circulation"] / 8760
        self.df["DHW"] = self.scaled_DHW_profile_circ + self.scaled_DHW_profile_draw_off

        self.DHW_sizing_power = self.get_DHW_sizing_power(self.building.n_Apartment) * (
                self.E_DHW * self.DHW_proportions["draw-off"] / 1e3)

    def __compute_load(self, drop_contributions):
        self.__compute_solar_gains()
        self.__compute_internal_gains()
        self.__compute_SC_demand()
        self.__compute_SH_demand()
        self.__compute_DHW_demand()
        self.df[["SH", "SC", "DHW"]] *= 1e-3  # in kWh
        if drop_contributions:
            self.df = self.df[["SH", "SC", "DHW"]]

    def __repr__(self):
        df = self.df.agg(["sum", "max"])
        # df.index = ["Annual (kWh/(m².year)", "Maximum (kW/m²)"]
        return repr(df)

