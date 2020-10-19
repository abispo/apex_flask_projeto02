from database import db

_session = db.session


def save(model):
    _session.add(model)
    _commit()
    return model


def delete(model):
    _session.delete(model)
    _commit()


def _commit():
    _session.commit()
