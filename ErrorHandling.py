from fastapi.responses import JSONResponse

def params_incorrect(param1,param2):
    return JSONResponse(
        status_code=400,
        content={"message":f"the {param1} and {param2} incorrect"},
    )

def town_and_pokimon_id_incorrect():
    return JSONResponse(
        status_code=400,
        content={"message":"the town and pokimonId incorrect"},
    )    


def the_param_incorrect(param):
    return JSONResponse(
        status_code=400,
        content={"message":f"the {param} incorrect"},
    ) 

def the_evolve_finished():
    return JSONResponse(
        status_code=400,
        content={"message":f"there is no more evolotion"},
    ) 