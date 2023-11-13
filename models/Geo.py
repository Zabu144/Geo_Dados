# pylint: disable=all

class Geo:
  def __init__(self,
               id,
               numOriginal,
               furo,
               geometalurgico,
               status,
               tipoMaterial,
               deCM,
               ateCM,
               profundidadePlanejada,
               alturaCone,
               profundidadeExecutada,
               presencaAgua,
               profundidadeAgua,
               tipoTerreno,
               deM,
               ateM,
               recuperacao,
               observacoes,
               data,
               turno,
               enviadoSGS):
    self.id = id
    self.numOriginal = numOriginal
    self.furo = furo
    self.geometalurgico = geometalurgico
    self.status = status
    self.tipoMaterial = tipoMaterial
    self.deCM = deCM
    self.ateCM = ateCM
    self.profundidadePlanejada = profundidadePlanejada
    self.alturaCone = alturaCone
    self.profundidadeExecutada = profundidadeExecutada
    self.presencaAgua = presencaAgua
    self.profundidadeAgua = profundidadeAgua
    self.tipoTerreno = tipoTerreno
    self.deM = deM
    self.ateM = ateM
    self.recuperacao = recuperacao
    self.observacoes = observacoes
    self.data = data
    self.turno = turno
    self.enviadoSGS = enviadoSGS
    