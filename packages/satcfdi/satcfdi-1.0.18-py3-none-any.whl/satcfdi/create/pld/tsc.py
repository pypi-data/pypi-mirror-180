from decimal import Decimal
from datetime import datetime, date, time
from collections.abc import Sequence
from ... import CFDI, XElement, ScalarMap


class FideicomisoSimpleType(ScalarMap):
    def __init__(
            self,
            denominacion_razon: str,
            rfc: str = None,
            identificador_fideicomiso: str = None,
    ): 
        """
        
        :param denominacion_razon:
        :param rfc:
        :param identificador_fideicomiso:
        """
        
        super().__init__({
            'DenominacionRazon': denominacion_razon,
            'Rfc': rfc,
            'IdentificadorFideicomiso': identificador_fideicomiso,
        })
        

class PersonaMoralSimpleType(ScalarMap):
    def __init__(
            self,
            denominacion_razon: str,
            fecha_constitucion: date = None,
            rfc: str = None,
            pais_nacionalidad: str = None,
    ): 
        """
        
        :param denominacion_razon:
        :param fecha_constitucion:
        :param rfc:
        :param pais_nacionalidad:
        """
        
        super().__init__({
            'DenominacionRazon': denominacion_razon,
            'FechaConstitucion': fecha_constitucion,
            'Rfc': rfc,
            'PaisNacionalidad': pais_nacionalidad,
        })
        

class PersonaFisicaSimpleType(ScalarMap):
    def __init__(
            self,
            nombre: str,
            apellido_paterno: str,
            apellido_materno: str,
            fecha_nacimiento: date = None,
            rfc: str = None,
            curp: str = None,
            pais_nacionalidad: str = None,
    ): 
        """
        
        :param nombre:
        :param apellido_paterno:
        :param apellido_materno:
        :param fecha_nacimiento:
        :param rfc:
        :param curp:
        :param pais_nacionalidad:
        """
        
        super().__init__({
            'Nombre': nombre,
            'ApellidoPaterno': apellido_paterno,
            'ApellidoMaterno': apellido_materno,
            'FechaNacimiento': fecha_nacimiento,
            'Rfc': rfc,
            'Curp': curp,
            'PaisNacionalidad': pais_nacionalidad,
        })
        

class TipoPersonaSimpleType(ScalarMap):
    def __init__(
            self,
            persona_fisica: PersonaFisicaSimpleType | dict = None,
            persona_moral: PersonaMoralSimpleType | dict = None,
            fideicomiso: FideicomisoSimpleType | dict = None,
    ): 
        """
        
        :param persona_fisica:
        :param persona_moral:
        :param fideicomiso:
        """
        
        super().__init__({
            'PersonaFisica': persona_fisica,
            'PersonaMoral': persona_moral,
            'Fideicomiso': fideicomiso,
        })
        

class DuenoBeneficiarioType(ScalarMap):
    def __init__(
            self,
            tipo_persona: TipoPersonaSimpleType | dict,
    ): 
        """
        
        :param tipo_persona:
        """
        
        super().__init__({
            'TipoPersona': tipo_persona,
        })
        

class TelefonoType(ScalarMap):
    def __init__(
            self,
            clave_pais: str = None,
            numero_telefono: str = None,
            correo_electronico: str = None,
    ): 
        """
        
        :param clave_pais:
        :param numero_telefono:
        :param correo_electronico:
        """
        
        super().__init__({
            'ClavePais': clave_pais,
            'NumeroTelefono': numero_telefono,
            'CorreoElectronico': correo_electronico,
        })
        

class ExtranjeroType(ScalarMap):
    def __init__(
            self,
            pais: str,
            estado_provincia: str,
            ciudad_poblacion: str,
            colonia: str,
            calle: str,
            numero_exterior: str,
            codigo_postal: str,
            numero_interior: str = None,
    ): 
        """
        
        :param pais:
        :param estado_provincia:
        :param ciudad_poblacion:
        :param colonia:
        :param calle:
        :param numero_exterior:
        :param codigo_postal:
        :param numero_interior:
        """
        
        super().__init__({
            'Pais': pais,
            'EstadoProvincia': estado_provincia,
            'CiudadPoblacion': ciudad_poblacion,
            'Colonia': colonia,
            'Calle': calle,
            'NumeroExterior': numero_exterior,
            'CodigoPostal': codigo_postal,
            'NumeroInterior': numero_interior,
        })
        

class NacionalType(ScalarMap):
    def __init__(
            self,
            colonia: str,
            calle: str,
            numero_exterior: str,
            codigo_postal: str,
            numero_interior: str = None,
    ): 
        """
        
        :param colonia:
        :param calle:
        :param numero_exterior:
        :param codigo_postal:
        :param numero_interior:
        """
        
        super().__init__({
            'Colonia': colonia,
            'Calle': calle,
            'NumeroExterior': numero_exterior,
            'CodigoPostal': codigo_postal,
            'NumeroInterior': numero_interior,
        })
        

class TipoDomicilioType(ScalarMap):
    def __init__(
            self,
            nacional: NacionalType | dict = None,
            extranjero: ExtranjeroType | dict = None,
    ): 
        """
        
        :param nacional:
        :param extranjero:
        """
        
        super().__init__({
            'Nacional': nacional,
            'Extranjero': extranjero,
        })
        

class RepresentanteApoderadoType(ScalarMap):
    def __init__(
            self,
            nombre: str,
            apellido_paterno: str,
            apellido_materno: str,
            fecha_nacimiento: date = None,
            rfc: str = None,
            curp: str = None,
    ): 
        """
        
        :param nombre:
        :param apellido_paterno:
        :param apellido_materno:
        :param fecha_nacimiento:
        :param rfc:
        :param curp:
        """
        
        super().__init__({
            'Nombre': nombre,
            'ApellidoPaterno': apellido_paterno,
            'ApellidoMaterno': apellido_materno,
            'FechaNacimiento': fecha_nacimiento,
            'Rfc': rfc,
            'Curp': curp,
        })
        

class FideicomisoType(ScalarMap):
    def __init__(
            self,
            denominacion_razon: str,
            apoderado_delegado: RepresentanteApoderadoType | dict,
            rfc: str = None,
            identificador_fideicomiso: str = None,
    ): 
        """
        
        :param denominacion_razon:
        :param apoderado_delegado:
        :param rfc:
        :param identificador_fideicomiso:
        """
        
        super().__init__({
            'DenominacionRazon': denominacion_razon,
            'ApoderadoDelegado': apoderado_delegado,
            'Rfc': rfc,
            'IdentificadorFideicomiso': identificador_fideicomiso,
        })
        

class PersonaMoralType(ScalarMap):
    def __init__(
            self,
            denominacion_razon: str,
            pais_nacionalidad: str,
            giro_mercantil: str,
            representante_apoderado: RepresentanteApoderadoType | dict,
            fecha_constitucion: date = None,
            rfc: str = None,
    ): 
        """
        
        :param denominacion_razon:
        :param pais_nacionalidad:
        :param giro_mercantil:
        :param representante_apoderado:
        :param fecha_constitucion:
        :param rfc:
        """
        
        super().__init__({
            'DenominacionRazon': denominacion_razon,
            'PaisNacionalidad': pais_nacionalidad,
            'GiroMercantil': giro_mercantil,
            'RepresentanteApoderado': representante_apoderado,
            'FechaConstitucion': fecha_constitucion,
            'Rfc': rfc,
        })
        

class PersonaFisicaType(ScalarMap):
    def __init__(
            self,
            nombre: str,
            apellido_paterno: str,
            apellido_materno: str,
            pais_nacionalidad: str,
            actividad_economica: str,
            fecha_nacimiento: date = None,
            rfc: str = None,
            curp: str = None,
    ): 
        """
        
        :param nombre:
        :param apellido_paterno:
        :param apellido_materno:
        :param pais_nacionalidad:
        :param actividad_economica:
        :param fecha_nacimiento:
        :param rfc:
        :param curp:
        """
        
        super().__init__({
            'Nombre': nombre,
            'ApellidoPaterno': apellido_paterno,
            'ApellidoMaterno': apellido_materno,
            'PaisNacionalidad': pais_nacionalidad,
            'ActividadEconomica': actividad_economica,
            'FechaNacimiento': fecha_nacimiento,
            'Rfc': rfc,
            'Curp': curp,
        })
        

class TipoPersonaType(ScalarMap):
    def __init__(
            self,
            persona_fisica: PersonaFisicaType | dict = None,
            persona_moral: PersonaMoralType | dict = None,
            fideicomiso: FideicomisoType | dict = None,
    ): 
        """
        
        :param persona_fisica:
        :param persona_moral:
        :param fideicomiso:
        """
        
        super().__init__({
            'PersonaFisica': persona_fisica,
            'PersonaMoral': persona_moral,
            'Fideicomiso': fideicomiso,
        })
        

class PersonaAvisoType(ScalarMap):
    def __init__(
            self,
            tipo_persona: TipoPersonaType | dict,
            tipo_domicilio: TipoDomicilioType | dict = None,
            telefono: TelefonoType | dict = None,
    ): 
        """
        
        :param tipo_persona:
        :param tipo_domicilio:
        :param telefono:
        """
        
        super().__init__({
            'TipoPersona': tipo_persona,
            'TipoDomicilio': tipo_domicilio,
            'Telefono': telefono,
        })
        

class AlertaType(ScalarMap):
    def __init__(
            self,
            tipo_alerta: str,
            descripcion_alerta: str = None,
    ): 
        """
        
        :param tipo_alerta:
        :param descripcion_alerta:
        """
        
        super().__init__({
            'TipoAlerta': tipo_alerta,
            'DescripcionAlerta': descripcion_alerta,
        })
        

class ModificatorioType(ScalarMap):
    def __init__(
            self,
            folio_modificacion: str,
            descripcion_modificacion: str,
    ): 
        """
        
        :param folio_modificacion:
        :param descripcion_modificacion:
        """
        
        super().__init__({
            'FolioModificacion': folio_modificacion,
            'DescripcionModificacion': descripcion_modificacion,
        })
        

class AvisoType(ScalarMap):
    def __init__(
            self,
            referencia_aviso: str,
            prioridad: str,
            alerta: AlertaType | dict,
            persona_aviso: PersonaAvisoType | dict | Sequence[PersonaAvisoType | dict],
            detalle_operaciones: DetalleOperacionesType | dict,
            modificatorio: ModificatorioType | dict = None,
            dueno_beneficiario: DuenoBeneficiarioType | dict | Sequence[DuenoBeneficiarioType | dict] = None,
    ): 
        """
        
        :param referencia_aviso:
        :param prioridad:
        :param alerta:
        :param persona_aviso:
        :param detalle_operaciones:
        :param modificatorio:
        :param dueno_beneficiario:
        """
        
        super().__init__({
            'ReferenciaAviso': referencia_aviso,
            'Prioridad': prioridad,
            'Alerta': alerta,
            'PersonaAviso': persona_aviso,
            'DetalleOperaciones': detalle_operaciones,
            'Modificatorio': modificatorio,
            'DuenoBeneficiario': dueno_beneficiario,
        })
        

class SujetoObligadoType(ScalarMap):
    def __init__(
            self,
            clave_sujeto_obligado: str,
            clave_actividad: str,
            clave_entidad_colegiada: str = None,
            exento: str = None,
    ): 
        """
        
        :param clave_sujeto_obligado:
        :param clave_actividad:
        :param clave_entidad_colegiada:
        :param exento:
        """
        
        super().__init__({
            'ClaveSujetoObligado': clave_sujeto_obligado,
            'ClaveActividad': clave_actividad,
            'ClaveEntidadColegiada': clave_entidad_colegiada,
            'Exento': exento,
        })
        

class InformeType(ScalarMap):
    def __init__(
            self,
            mes_reportado: str,
            sujeto_obligado: SujetoObligadoType | dict,
            aviso: AvisoType | dict | Sequence[AvisoType | dict] = None,
    ): 
        """
        
        :param mes_reportado:
        :param sujeto_obligado:
        :param aviso:
        """
        
        super().__init__({
            'MesReportado': mes_reportado,
            'SujetoObligado': sujeto_obligado,
            'Aviso': aviso,
        })
        

class ArchivoType(ScalarMap):
    def __init__(
            self,
            informe: InformeType | dict | Sequence[InformeType | dict],
    ): 
        """
        
        :param informe:
        """
        
        super().__init__({
            'Informe': informe,
        })
        

class DatosOperacionType(ScalarMap):
    def __init__(
            self,
            fecha_periodo: str,
            tipo_operacion: str,
            tipo_tarjeta: str,
            numero_identificador: str,
            monto_gasto: str,
    ): 
        """
        
        :param fecha_periodo:
        :param tipo_operacion:
        :param tipo_tarjeta:
        :param numero_identificador:
        :param monto_gasto:
        """
        
        super().__init__({
            'FechaPeriodo': fecha_periodo,
            'TipoOperacion': tipo_operacion,
            'TipoTarjeta': tipo_tarjeta,
            'NumeroIdentificador': numero_identificador,
            'MontoGasto': monto_gasto,
        })
        

class DetalleOperacionesType(ScalarMap):
    def __init__(
            self,
            datos_operacion: DatosOperacionType | dict | Sequence[DatosOperacionType | dict],
    ): 
        """
        
        :param datos_operacion:
        """
        
        super().__init__({
            'DatosOperacion': datos_operacion,
        })
        

class Archivo(ArchivoType, XElement):
    tag = '{http://www.uif.shcp.gob.mx/recepcion/tsc}archivo'

