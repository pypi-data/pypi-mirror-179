from viggocore.database import db
from viggocore.common.subsystem import entity


class FormaPagamentoSefaz(entity.Entity, db.Model):

    attributes = ['codigo', 'descricao']
    attributes += entity.Entity.attributes

    codigo = db.Column(db.CHAR(2), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    def __init__(self, id, codigo, descricao,
                 active=True, created_at=None, created_by=None,
                 updated_at=None, updated_by=None, tag=None):
        super().__init__(id, active, created_at, created_by,
                         updated_at, updated_by, tag)
        self.codigo = codigo
        self.descricao = descricao
