from typing import Any, ClassVar, List, Union

import _thread
import collections
import typing
List: typing._SpecialGenericAlias
Union: typing._SpecialForm
_cache_getAllAdsorptionAndAbsorptionNames: list
_cache_getAllCondensingGasNames: list
_cache_getAllGasNames: list
_cache_getAllLiquidNames: list
_cache_getAllVLEFluidNames: list
_destructor_queue: collections.deque
_logger_wrapper_backup: None
_tilmedia_lock: _thread.lock
deepcopy: function

class CLoggerWrapper:
    """
    Wrapper for the C message functions, to get the actual function pointer.
    """
    format_error: Any
    format_message: Any
    id: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class ExternalObject:
    ptr: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class LoggerWrapper:
    """
    Wrapper class for the logger. It holds the exceptions, the C wrapper, and the message functions.
    """
    __init__: ClassVar[function] = ...
    @property
    def format_error(self) -> Any: ...
    @property
    def format_message(self) -> Any: ...

class TILMediaError(Exception):
    """
    TILMedia Error without further specification.
    """
    __init__: ClassVar[function] = ...
    with_traceback: ClassVar[function] = ...

def BatchFunctionCaller_abort(*args, **kwargs) -> Any: ...
def BatchFunctionCaller_currentPoint(*args, **kwargs) -> Any: ...
def BatchFunctionCaller_execute(*args, **kwargs) -> Any: ...
def GasObjectFunctions_freezingPoint(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificAbsoluteGasEntropy_pTn(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificAbsoluteLiquidEntropy_pTn(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificAbsoluteSolidEntropy_pTn(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificGasEnthalpy_refStateHf_Tn(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificLiquidEnthalpy_refStateHf_Tn(*args, **kwargs) -> Any: ...
def GasObjectFunctions_specificSolidEnthalpy_refStateHf_Tn(*args, **kwargs) -> Any: ...
def Gas_isValid_getInfo_errorInterface(*args, **kwargs) -> Any: ...
def Gas_maximalTemperature(*args, **kwargs) -> Any: ...
def Gas_minimalTemperature(*args, **kwargs) -> Any: ...
def Gas_molarMass(*args, **kwargs) -> Any: ...
def Liquid_isValid_getInfo_errorInterface(*args, **kwargs) -> Any: ...
def Liquid_maximalTemperature_xi_(*args, **kwargs) -> Any: ...
def Liquid_minimalTemperature_xi_(*args, **kwargs) -> Any: ...
def VLEFluidFunctions_density_pTxi(*args, **kwargs) -> Any: ...
def VLEFluid_Cached_molarMass(*args, **kwargs) -> Any: ...
def VLEFluid_isValid_getInfo_errorInterface(*args, **kwargs) -> Any: ...
def __pyx_unpickle_Enum(*args, **kwargs) -> Any: ...
def clear_medium_name_cache(*args, **kwargs) -> Any:
    """
    Clear the name cache. This might be required if the data path has been changed.
    """
def getGasInformation_pointer(*args, **kwargs) -> Any: ...
def getLiquidInformation_pointer(*args, **kwargs) -> Any: ...
def getVLEFluidInformation_pointer(*args, **kwargs) -> Any: ...
def get_all_adsorption_and_absorption_names(*args, **kwargs) -> Any:
    """
    Get the list of medium names

    Returns:
        list: list of medium names
    """
def get_all_condensing_gas_names(*args, **kwargs) -> Any:
    """
    Get the list of Condensing Gas names

    Returns:
        list: list of Condensing Gas names
    """
def get_all_gas_names(*args, **kwargs) -> Any:
    """
    Get the list of Gas names

    Returns:
        list: list of Gas names
    """
def get_all_liquid_names(*args, **kwargs) -> Any:
    """
    Get the list of Liquid names

    Returns:
        list: list of Liquid names
    """
def get_all_vleFluid_names(*args, **kwargs) -> Any:
    """
    Get the list of VLEFluid names

    Returns:
        list: list of VLEFluid names
    """
def get_closest_vleFluid_dpT(*args, **kwargs) -> Any:
    """
    detect medium name for a given critical point of a VLEFluid

    Args:
        d (float): critical density
        p (float): critical pressure
        T (float): critical temperature

    Returns:
        str: medium name
    """
def get_data_path(*args, **kwargs) -> Any:
    """
    Get the TILMediaDataPath

    Returns:
        str : Data path of TILMedia
    """
def get_fit_config(*args, **kwargs) -> Any: ...
def get_fit_config_eo(*args, **kwargs) -> Any: ...
def get_fit_data(*args, **kwargs) -> Any: ...
def get_fit_data_eo(*args, **kwargs) -> Any: ...
def get_fluid_information(*args, **kwargs) -> Any: ...
def get_fluid_information_eo(*args, **kwargs) -> Any: ...
def license_is_valid(*args, **kwargs) -> Any:
    """
    Check if the TILMedia License is valid.
    """
def set_data_path(*args, **kwargs) -> Any:
    """
    Set the TILMediaDataPath

    Args:
        path (str): Data path of TILMedia
    """
