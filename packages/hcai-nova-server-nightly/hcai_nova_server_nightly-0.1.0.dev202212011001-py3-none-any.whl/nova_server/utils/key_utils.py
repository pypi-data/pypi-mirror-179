

def get_key_from_request_form(request_form):
    return request_form['username'] + '_' + request_form['database'] + '_' + request_form['scheme'] + '_' + \
           request_form['streamName'] + '_' + request_form['annotator'] + '_' + \
           request_form['sessions']
           #+ '_' + request_form['trainerName'] + '_' + \
           #request_form['mode']
