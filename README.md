# Pet rock simulator                                                         
A game where you take care of your pet rock, name it and take care of it.                                                                                                         
Pay attention to its weight, energy, and hunger                                                                                

## How to run
1. Use Python 3.6 or a higher version.
2. Run the script: python rock_simulator.py
3. Enter your name and rocks name
4. You will see the rocks stats each turn
5. Choose an action
6. Random events may occur

## Game Over Conditions

Your rock won’t last forever. The game ends if:                                                                                 
Hunger reaches 10 → your rock crumbles                                                                                                                                             
Energy drops to 0 → it turns into gravel                                                                                                                                             
Weight drops to 0 → it erodes into sand                                                                                                                                          
Weight reaches 10 → it sinks into the earth                                                                                                                                                                                                     


### Example 
<img width="747" height="438" alt="image" src="https://github.com/user-attachments/assets/0ad146cc-4c1e-409d-bd61-c39b59aa964b" />


### notes
Every playthrough will be different because of random events.















## This is my decision tree for my pet rock game
START                                                                                                           
│                                                                                                                          
├── Input player_name                                                                                              
├── Input rock_name                                                                                                 
│                                                                                                          
└── Initialize stats: hunger=5, energy=5, weight=5                                                                                             
     │                                                                                                            
 LOOP (while True)                                                                                                                            
     │                                                                                                          
     ├── Show Stats (hunger, energy, weight)                                                                                             
     ├── Show Menu (1–6)                                                                                                            
     │                                                                                                                    
     ├── Player Choice                                                                                                  
     │    ├── [1] Feed Rock                                                                                                 
     │    │     ├── hunger -2                                                                                         
     │    │     └── weight +1                                                                           
     │    │                                                                                             
     │    ├── [2] Rest                                                                                           
     │    │     ├── energy +2                                                                                              
     │    │     └── hunger +1                                                                             
     │    │                                                                                              
     │    ├── [3] Walk                                                                                  
     │    │     ├── weight -1                                                                                       
     │    │     └── energy -2                                                                   
     │    │                                                                                                                            
     │    ├── [4] Play                                                                                                 
     │    │     ├── hunger +1                                                                                                            
     │    │     └── energy -1                                                                                            
     │    │
     │    ├── [5] Do Nothing                                                                       
     │    │     ├── hunger +1                                                                              
     │    │     └── energy -1                                                                         
     │    │                                                                                                       
     │    ├── [6] Quit → END GAME                                                                                      
     │    │                                                                                                      
     │    └── Else → "Invalid Choice"                                                                                          
     │                                                                                                            
     ├── Random Event? (20% chance)                                                                                                            
     │    └── Show random funny event                                                                                                                   
     │                                                                                                                              
     ├── Clamp Stats (hunger 0–10, energy 0–10, weight 1–10)                                                                                         
     │
     ├── Check End Conditions                                                                                          
     │    ├── hunger >= 10 → Rock crumbles                                                                                                                
     │    ├── energy <= 0 → Rock turns to gravel                                                                                            
     │    ├── weight <= 0 → Rock erodes to sand                                                                                                           
     │    └── weight >= 10 → Rock sinks into earth                                                                                  
     │                                                                                                                                                                    
     └── If no end condition → loop continues                                                                                                                 
