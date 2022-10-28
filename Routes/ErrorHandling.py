from fastapi.responses import JSONResponse

def params_incorrect(param1,param2):
    return JSONResponse(
        status_code=400,
        content={"message":f"the {param1} and {param2} incorrect"},
    )

def the_same_type():
    return JSONResponse(
        status_code=400,
        content={"message":f"the trainer alredy have one eith this type"},
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

def the_row_dosent_excit():
    return JSONResponse(
        status_code=400,
        content={"message":f"the row dosent excit incorrect"},
) 