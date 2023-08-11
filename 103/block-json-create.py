from prefect import flow
from prefect.blocks.system import JSON

autos = JSON(value=dict(newcars=["tesla", "fiat"], trucks=["rivian", "ford"]))
autos.save(name="json-block-exbis", overwrite=True)

# careful not try to save with capital letters or underscores or spaces!


@flow
def get_newcars():
    json_block = JSON.load("json-block-exbis")
    print(json_block.value["newcars"])


get_newcars()
