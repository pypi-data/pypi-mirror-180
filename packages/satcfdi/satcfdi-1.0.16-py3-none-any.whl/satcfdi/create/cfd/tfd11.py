from datetime import datetime

from ...cfdi import CFDI, XElement, MEXICO_TZ
from ...models.signer import Signer


class TimbreFiscalDigital(CFDI):
    """
    Complemento requerido para el Timbrado Fiscal Digital que da validez al Comprobante fiscal digital por Internet.
    """
    tag = '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital'
    version = '1.1'

    def __init__(
            self,
            proveedor: Signer,
            uuid: str,
            fecha_timbrado: datetime,
            sello_cfd: str,
            leyenda: str = None,
    ):
        """
        Complemento requerido para el Timbrado Fiscal Digital que da valides a un Comprobante Fiscal Digital.

        :param uuid: Atributo requerido para expresar los 36 caracteres del UUID de la transacción de timbrado
        :param fecha_timbrado: Atributo requerido para expresar la fecha y hora de la generación del timbre
        :param sello_cfd: Atributo requerido para contener el sello digital del comprobante fiscal, que será timbrado. El sello deberá ser expresado cómo una cadena de texto en formato Base 64.
        :param no_certificado_sat: Atributo requerido para expresar el número de serie del certificado del SAT usado para el Timbre
        :param sello_sat: Atributo requerido para contener el sello digital del Timbre Fiscal Digital, al que hacen referencia las reglas de resolución miscelánea aplicable. El sello deberá ser expresado cómo una cadena de texto en formato Base 64.
        :return: objeto CFDI
        """

        super().__init__({
            'Version': self.version,
            'UUID': uuid,
            'FechaTimbrado': fecha_timbrado or datetime.now(tz=MEXICO_TZ).replace(tzinfo=None),
            'RfcProvCertif': proveedor.rfc_pac,
            'SelloCFD': sello_cfd,
            'NoCertificadoSAT': proveedor.certificate_number,
            'SelloSAT': '',
            'Leyenda': leyenda,
        })

        self['SelloSAT'] = proveedor.sign_sha256(
            self.cadena_original().encode()
        )
