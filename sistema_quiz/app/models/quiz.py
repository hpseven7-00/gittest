class Quiz(db.Model):
    from app.database.connection import db


    __tablename__ = "quizzes"

    NIVEIS = ["facil","medio","dificil"]

    id = db.Column(db.Integer, primar_key=True)
    titulo = db.Column(db.String(150),  nullable = False)
    descricao = db.Column(db.String(255),  nullable = True)
    nivel = db.Column(db.String(20), nullable=False, default = "medio")
    disicplina_id = db.Column(db.Integer, db.Foreignkey("disciplinas.id"))

    questoes = db.relationships("Quiz", backref="disciplina", lazy=True, cascade = "all, delete-orphan")
    resultados = db.relationships("Quiz", backref="disciplina", lazy=True, cascade = "all, delete-orphan")


    def calcular_pontuacao(self, respostas: dict) -> dict:



        total = len(self.questoes)
        if total == 0:
            return ("acertos": 0, "total": 0, "percentual", 0.0)