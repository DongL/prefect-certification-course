from prefect.blocks.system import Secret

secret_block = Secret.load("my-secret")
print(secret_block.get())
