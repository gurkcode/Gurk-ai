from brain.memory import load_memory, add_memory
from brain.thinker import think

memory = load_memory()

print("gurk online")

while True:
    user = input("human: ")

    reply = think(user)

    print("gurk:", reply)

    add_memory(memory, {"human": user, "guck": reply})


 Future Plans

- autonomous internet observation  
- X / Twitter bot  
- AI personality experiments  



built for fun. built for chaos.
