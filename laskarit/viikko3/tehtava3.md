```mermaid

sequenceDiagram
  main ->> Machine: Machine()
  Machine ->> FuelTank: FuelTank()
  Machine ->> FuelTank: tank.fill(40)
  Machine ->> Engine: Engine(FuelTank())
  main ->> Machine: drive()
  activate Machine
  Machine ->> Engine: start()
  activate Engine
  Engine ->> FuelTank: consume(5)
  deactivate Engine
  Machine ->> Engine: is_running()
  activate Engine
  Engine ->> FuelTank: .fuel_contents
  FuelTank -->> Engine: 35
  Engine -->> Machine: True
  deactivate Engine
  Machine ->> Engine: use_energy()
  Engine ->> FuelTank: _fuel_tank.consume(10)
  Machine -->> main: _
  deactivate Machine
  
  ```
