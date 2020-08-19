from euclidean_space import *
from colors import color
from matrices import matrix
import math




screen_config = {'center':coordinate(0,0,0),
                 'screen_dist':1,
                 'screen_pitch':90,
                 'screen_yaw':0,
                 'lenght':4,
                 'width':2,
                 'pixel_per_unit':20}


def degree_to_rad(deg):
    return (deg*math.pi)/180

def rad_to_degree(rad):
    return (rad*180)/math.pi

def creat_ray(screen_config):
    
    def spherical_coordinates(dist,pitch,yaw):
        x = dist*math.cos(pitch)*math.cos(yaw)
        y = dist*math.sin(pitch)
        z = dist*math.cos(pitch)*math.sin(yaw)
        return coordinate(x,y,z)
    
    screen_config["screen_pitch"] = degree_to_rad(screen_config["screen_pitch"])
    screen_config["screen_yaw"] = degree_to_rad(screen_config["screen_yaw"])
    
    center_vector = spherical_coordinates(screen_config["screen_dist"],screen_config["screen_pitch"],screen_config["screen_yaw"]).to_vector()
    
    top_left = spherical_coordinates(screen_config["width"],screen_config["screen_pitch"]+math.pi/2,screen_config["screen_yaw"]).to_vector()
    
    bottom_right = spherical_coordinates(screen_config["lenght"],0,math.pi/2-screen_config["screen_yaw"]).to_vector()
    
    bottom_left = center_vector-(top_left/2)-(bottom_right/2)

    for y_px in range(screen_config["width"]*screen_config["pixel_per_unit"]):
        for x_px in range(screen_config["lenght"]*screen_config["pixel_per_unit"]):
            
            created_vect = bottom_left + (y_px/(screen_config["width"]*screen_config["pixel_per_unit"]))*top_left + (x_px/(screen_config["lenght"]*screen_config["pixel_per_unit"]))*bottom_right
            
            
            
            created_ray = ray(screen_config["center"],created_vect)
            
            yield created_ray
        
