from prefect.blocks.system import Secret

my_secret_block = Secret(value="shhh!-it's-a-secret")
my_secret_block.save(name="secret-thing", overwrite=True)


my_secret_thing = Secret.load("secret-thing")
print(my_secret_thing)
print(my_secret_thing.get())
