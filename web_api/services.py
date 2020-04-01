import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    return None

def get_episodes(ep_id,params={}):
    if ep_id:
        response = generate_request(f"https://rickandmortyapi.com/api/episode/{ep_id}", params)
    else:
        response = generate_request('https://rickandmortyapi.com/api/episode/', params)
    if response:
        if (ep_id and len(ep_id) == 1):
            for ep in range(len(response)):
                list_pj = []
                for pj in response[ep]['characters']:
                    list_pj.append(int(pj.split('/')[-1]))
                response_pjs = requests.get(f"https://rickandmortyapi.com/api/character/{list_pj}").json()
                response[ep]['personajes'] = response_pjs
            episodes = response
        elif ep_id:
            episodes = response
        else:
            episodes = response.get('results')
        return episodes

    return 'error'

def get_characters(pj_id, params={}):
    if pj_id:
        response = generate_request(f'https://rickandmortyapi.com/api/character/{pj_id}', params)
    else:
        response = generate_request('https://rickandmortyapi.com/api/character/', params)
    if response:
        if pj_id and len(pj_id) == 1:
            list_ep = []
            for ep in response[0]['episode']:
                list_ep.append(int(ep.split('/')[-1]))
            response_ep = requests.get(f"https://rickandmortyapi.com/api/episode/{list_ep}").json()
            response[0]['episodios'] = response_ep

            if (response[0]['origin']['url'] != ""):
                origen_id = int(response[0]['origin']['url'].split('/')[-1])
                res_origen = requests.get(f"https://rickandmortyapi.com/api/location/{[origen_id]}").json()
                response[0]['origen'] = res_origen[0]
            else:
                response[0]['origen'] = {'id': 0, 'name': 'Desconocido'}


            if (response[0]['location']['url'] != ""):
                lugar_actual_id = int(response[0]['location']['url'].split('/')[-1])
                res_actual = requests.get(f"https://rickandmortyapi.com/api/location/{[lugar_actual_id]}").json()
                response[0]['lugar'] = res_actual[0]
            else:
                response[0]['lugar'] = {'id': 0, 'name': 'Desconocido'}

            characters = response
        elif pj_id:
            characters = response
        else:
            characters = response.get('results')
        return characters

    return ''

def get_locations(loc_id, params={}):
    if loc_id:
        response = generate_request(f'https://rickandmortyapi.com/api/location/{loc_id}', params)
    else:
        response = generate_request('https://rickandmortyapi.com/api/location/', params)
    if response:
        if loc_id and len(loc_id) == 1:
            list_pj = []
            for pj in response[0]['residents']:
                list_pj.append(int(pj.split('/')[-1]))
            response_pjs = requests.get(f"https://rickandmortyapi.com/api/character/{list_pj}").json()
            response[0]['residentes'] = response_pjs
            locations = response
        elif loc_id:
            locations = response
        else:
            locations = response.get('results')
        return locations

    return ''

def get_info(name, params={}):
    response_pjs = generate_request(f'https://rickandmortyapi.com/api/character/?name={name}', params)
    response_loc = generate_request(f'https://rickandmortyapi.com/api/location/?name={name}', params)
    response_eps = generate_request(f"https://rickandmortyapi.com/api/episode/?name={name}", params)

    paginas_pjs = []
    paginas_loc = []
    paginas_eps = []

    if response_pjs:
        paginas_pjs.append(response_pjs.get('results'))
        while response_pjs['info']['next'] != "":
            response_pjs = generate_request(response_pjs['info']['next'], params)
            paginas_pjs.append(response_pjs.get('results'))
    else:
        paginas_pjs.append(response_pjs)
    
    if response_loc:
        paginas_loc.append(response_loc.get('results'))
        while response_loc['info']['next'] != "":
            response_loc = generate_request(response_loc['info']['next'], params)
            paginas_loc.append(response_loc.get('results'))
    else:
        paginas_loc.append(response_loc)
    
    if response_eps:
        paginas_eps.append(response_eps.get('results'))
        while response_eps['info']['next'] != "":
            response_eps = generate_request(response_eps['info']['next'], params)
            paginas_eps.append(response_eps.get('results'))
    else:
        paginas_eps.append(response_eps)

    return [paginas_pjs, paginas_loc, paginas_eps]

    

