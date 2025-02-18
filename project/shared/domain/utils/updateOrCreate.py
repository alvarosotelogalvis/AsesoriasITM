def update_or_create(session, model, keys: dict = {}, data: dict = None):
    element_model = session.query(model).filter_by(**keys).first()
    if element_model:
        for key, value in data.items():
            if key not in keys:
                setattr(element_model, key, value)
        session.commit()
        
        return element_model

    element_model = model(**{**keys, **data})
    session.add(element_model)
    session.commit()
    session.refresh(element_model)

    return element_model
