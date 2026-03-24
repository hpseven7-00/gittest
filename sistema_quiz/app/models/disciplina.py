
from app.database.connection import db

class Disciplina(db.Model):
    __tablename__ = "disciplinas"

    id = db.Column(db.Integer, primar_key=True)
    nome = db.Column(db.String(100),  nullable = False, unique = True)
    descricao = db.Column(db.String(255),  nullable = True)

    quizzes = db.relationships("Quiz", backref="disciplina",
                               lazy=True, cascade = "all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
        }

