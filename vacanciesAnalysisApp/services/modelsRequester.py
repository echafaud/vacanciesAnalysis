def InsertData(model, data):
    modelData = model.objects.all()
    modelData.delete()
    model.objects.bulk_create(
        model(**vals) for vals in data.to_dict('records')
    )
