

def form_to_instance(form, obj):    
    for attr in dict(form):
        try:            
            setattr(obj, attr, form[attr])
        except Exception as e:
            print e

    return obj