from ..models import Measurements
from ..models import Variable


def get_measurements():
    measurements = Measurements.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement=Measurements.objects.get(pk=var_pk)
    return measurement

def update_measurement_unit(var_pk,new_var):
    measurement=get_measurement(var_pk)
    measurement.unit=new_var["unit"]
    measurement.save()
    return measurement

def update_measurement_value(var_pk,new_var):
    measurement=get_measurement(var_pk)
    measurement.value=new_var["value"]
    measurement.save()
    return measurement

def update_measurement_variable(var_pk,new_var):
    measurement=get_measurement(var_pk)
    measurement.Variable=new_var["variable"]
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement=get_measurement(var_pk)
    nombre=measurement.name
    measurement.delete()
    return nombre


def create_Measurement(var):
    print(var)
    variable = Variable.objects.get(pk=var["Variable"])
    measurement = Measurements(Variable=variable,value=var["value"],unit=var["unit"],place=var["place"])
    measurement.save()
    return measurement



