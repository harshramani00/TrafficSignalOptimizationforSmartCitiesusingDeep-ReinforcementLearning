import os
import subprocess
import sys

import subprocess

import subprocess

import traci

def create_sumo_files():
    # Create nodes file with traffic lights
    with open('my_nodes.nod.xml', 'w') as f:
        f.write('''<nodes>
    <node id="1" x="0" y="0" type="priority"/>
    <node id="2" x="100" y="0" type="priority"/>
    <node id="3" x="25" y="50" type="priority"/>
    <node id="4" x="25" y="-50" type="priority"/>
    <node id="5" x="75" y="50" type="priority"/>
    <node id="6" x="75" y="-50" type="priority"/>
    <node id="7" x="25" y="0" type="traffic_light"/>
    <node id="8" x="75" y="0" type="traffic_light"/>
                
    <node id="e1" x="0" y="25" type="priority"/>
    <node id="e2" x="25" y="0" type="priority"/>
</nodes>''')

    # Create edges file
    with open('my_edges.edg.xml', 'w') as f:
        f.write('''<edges>
    <edge id="1to7" from="1" to="7" priority="1" numLanes="2" speed="13.89"/>
    <edge id="7to8" from="7" to="8" priority="1" numLanes="2" speed="13.89"/>
    <edge id="8to2" from="8" to="2" priority="1" numLanes="2" speed="13.89"/>
    <edge id="2to8" from="2" to="8" priority="1" numLanes="2" speed="13.89"/>
    <edge id="8to7" from="8" to="7" priority="1" numLanes="2" speed="13.89"/>
    <edge id="7to1" from="7" to="1" priority="1" numLanes="2" speed="13.89"/>
    <edge id="3to7" from="3" to="7" priority="1" numLanes="2" speed="13.89"/>
    <edge id="7to4" from="7" to="4" priority="1" numLanes="2" speed="13.89"/>
    <edge id="4to7" from="4" to="7" priority="1" numLanes="2" speed="13.89"/>
    <edge id="7to3" from="7" to="3" priority="1" numLanes="2" speed="13.89"/>
    <edge id="5to8" from="5" to="8" priority="1" numLanes="2" speed="13.89"/>
    <edge id="8to6" from="8" to="6" priority="1" numLanes="2" speed="13.89"/>
    <edge id="6to8" from="6" to="8" priority="1" numLanes="2" speed="13.89"/>
    <edge id="8to5" from="8" to="5" priority="1" numLanes="2" speed="13.89"/>
                
    <edge id="e1to7" from="e1" to="7" priority="1" numLanes="1" speed="20.0"/>
    <edge id="7toe1" from="7" to="e1" priority="1" numLanes="1" speed="20.0"/>
</edges>''')

    # Generate network file using netconvert
    subprocess.run(['netconvert', '--node-files=my_nodes.nod.xml', '--edge-files=my_edges.edg.xml', '--output-file=my_network.net.xml', '--tls.guess', '--tls.default-type', 'static'])

    # Create routes file with more vehicles
    with open('my_routes.rou.xml', 'w') as f:
        f.write('''<routes>
                
     <!-- Vehicles -->     
                      
    <vType id="car" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>
    <vType id="emergency_car" accel="1.2" decel="6.0" sigma="0.5" length="6" minGap="2.5" maxSpeed="25.0" guiShape="emergency"/>

    <!-- Common Routes -->
                           
    <route id="route0" edges="1to7 7to8 8to2"/>
    <route id="route1" edges="2to8 8to7 7to1"/>
    <route id="route2" edges="3to7 7to4"/>
    <route id="route3" edges="4to7 7to3"/>
    <route id="route4" edges="5to8 8to6"/>
    <route id="route5" edges="6to8 8to5"/>
                

    <!-- Emergency Routes -->
                        
    <route id="emergency_route1" edges="e1to7 7to8 8to2"/>
    <route id="emergency_route2" edges=" 2to8 8to7 7toe1"/>  
              


    <!-- Complex Routes -->
                               
    <route id="complex_route1" edges="1to7 7to4"/>
    <route id="complex_route2" edges="1to7 7to3"/>
    <route id="complex_route3" edges="1to7 7to8 8to6"/>  
    <route id="complex_route4" edges="1to7 7to8 8to5"/>
    <route id="complex_route5" edges="1to7 7to8 8to2"/>         
    
    <route id="complex_route6" edges="2to8 8to6"/>'
    <route id="complex_route7" edges="2to8 8to5"/>
    <route id="complex_route8" edges="2to8 8to7 7to4"/>
    <route id="complex_route9" edges="2to8 8to7 7to3"/>
    <route id="complex_route10" edges="2to8 8to7 7to1"/>

    <route id="complex_route11" edges="3to7 7to8 8to6"/>
    <route id="complex_route12" edges="3to7 7to8 8to5"/>
    <route id="complex_route13" edges="3to7 7to8 8to2"/>
    <route id="complex_route14" edges="3to7 7to4"/>

    <route id="complex_route15" edges="4to7 7to8 8to6"/>
    <route id="complex_route16" edges="4to7 7to8 8to5"/>
    <route id="complex_route17" edges="4to7 7to8 8to2"/>
    <route id="complex_route18" edges="4to7 7to3"/>

    <route id="complex_route19" edges="5to8 8to2"/>
    <route id="complex_route20" edges="5to8 8to7 7to4"/>
    <route id="complex_route21" edges="5to8 8to7 7to3"/>
    <route id="complex_route22" edges="5to8 8to6"/>

    <route id="complex_route23" edges="6to8 8to2"/>
    <route id="complex_route24" edges="6to8 8to7 7to4"/>
    <route id="complex_route25" edges="6to8 8to7 7to3"/>
    <route id="complex_route26" edges="6to8 8to5"/>
 
                
    <!-- Flows -->
                            
    <flow id="flow0" type="car" route="route0" begin="0" end="3600" vehsPerHour="100"/>
    <flow id="flow1" type="car" route="route1" begin="0" end="3600" vehsPerHour="100"/>
    <flow id="flow2" type="car" route="route2" begin="0" end="3600" vehsPerHour="200"/>
    <flow id="flow3" type="car" route="route3" begin="0" end="3600" vehsPerHour="200"/>
    <flow id="flow4" type="car" route="route4" begin="0" end="3600" vehsPerHour="200"/>
    <flow id="flow5" type="car" route="route5" begin="0" end="3600" vehsPerHour="100"/>
            
    <flow id="emergency_flow1" type="emergency_car" route="emergency_route1" begin="0" end="3600" vehsPerHour="6"/>
    <flow id="emergency_flow2" type="emergency_car" route="emergency_route2" begin="0" end="3600" vehsPerHour="6"/>
                
    <flow id="complex_flow1" type="car" route="complex_route1" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow2" type="car" route="complex_route2" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow3" type="car" route="complex_route3" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow4" type="car" route="complex_route4" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow5" type="car" route="complex_route5" begin="0" end="3600" vehsPerHour="50"/>
                
    <flow id="complex_flow6" type="car" route="complex_route6" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow7" type="car" route="complex_route7" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow8" type="car" route="complex_route8" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow9" type="car" route="complex_route9" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow10" type="car" route="complex_route10" begin="0" end="3600" vehsPerHour="250"/>
                
    <flow id="complex_flow11" type="car" route="complex_route11" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow12" type="car" route="complex_route12" begin="0" end="3600" vehsPerHour="250"/>
    <flow id="complex_flow13" type="car" route="complex_route13" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow14" type="car" route="complex_route14" begin="0" end="3600" vehsPerHour="50"/>
    
    <flow id="complex_flow15" type="car" route="complex_route15" begin="0" end="3600" vehsPerHour="250"/>
    <flow id="complex_flow16" type="car" route="complex_route16" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow17" type="car" route="complex_route17" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow18" type="car" route="complex_route18" begin="0" end="3600" vehsPerHour="50"/>
                
    <flow id="complex_flow19" type="car" route="complex_route19" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow20" type="car" route="complex_route20" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow21" type="car" route="complex_route21" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow22" type="car" route="complex_route22" begin="0" end="3600" vehsPerHour="250"/>
    
    <flow id="complex_flow23" type="car" route="complex_route23" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow24" type="car" route="complex_route24" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow25" type="car" route="complex_route25" begin="0" end="3600" vehsPerHour="50"/>
    <flow id="complex_flow26" type="car" route="complex_route26" begin="0" end="3600" vehsPerHour="50"/>
                        
</routes>''')

    # Create SUMO configuration file
    with open('my_simulation.sumocfg', 'w') as f:
        f.write('''<configuration>
    <input>
        <net-file value="my_network.net.xml"/>
        <route-files value="my_routes.rou.xml"/>
    </input>
    <time>
        <begin value="0"/>
        <end value="3600"/>
    </time>
    <report>
        <verbose value="true"/>
        <no-step-log value="true"/>
    </report>
</configuration>''')


def start_sumo():
    sumoBinary = 'sumo-gui'  # or 'sumo' for command line
    sumoCmd = [sumoBinary, '-c', 'my_simulation.sumocfg']
    traci.start(sumoCmd)

def check_simulation():
    try:
        start_sumo()
        print("Simulation loaded successfully.")
        
        traffic_lights = traci.trafficlight.getIDList()
        print(f'Traffic light IDs: {traffic_lights}')

        simulation_steps = 1000
        for step in range(simulation_steps):
            traci.simulationStep()
            
            vehicles = traci.vehicle.getIDList()
            emergency_vehicles = [v for v in vehicles if traci.vehicle.getTypeID(v) == 'emergency_car']
            
            for tl_id in traffic_lights:
                controlled_lanes = traci.trafficlight.getControlledLanes(tl_id)
                for ev in emergency_vehicles:
                    lane_id = traci.vehicle.getLaneID(ev)
                    if lane_id in controlled_lanes:
                        # Check current phase and adjust only if it doesn't disrupt regular flow excessively
                        current_phase = traci.trafficlight.getPhase(tl_id)
                        if current_phase != 0:  # Assuming phase 0 is for emergency vehicle priority
                            # Logic to decide whether to switch phase based on current traffic conditions
                            # For example, only switch if the queue length is below a certain threshold
                            queue_length = sum(traci.lane.getLastStepVehicleNumber(lane) for lane in controlled_lanes)
                            if queue_length < 10:  # Example threshold
                                print(f'Emergency vehicle {ev} detected near traffic light {tl_id}. Adjusting priority.')
                                traci.trafficlight.setPhase(tl_id, 0)
                            else:
                                print(f'Emergency vehicle {ev} detected but not prioritizing due to high queue length.')
                        break

        traci.close()
        print("Simulation completed.")
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    if 'SUMO_HOME' not in os.environ:
        print("Please set the SUMO_HOME environment variable")
        exit(1)

    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)

    create_sumo_files()
    print("SUMO files created successfully.")

    check_simulation()