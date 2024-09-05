#a auto driving car 
#can detect object
#can decide itself where to move
#can set destinction location.
#implement battery in the car
#automatic charge

class Battery:
   
    def show_battery_percetage(self):
        return 49 #random

    def solar_charge(self):
        self.is_solar_charging = True

    def stop_solar_charge(self):
        self.is_solar_charging = False

    def charge(self):
        pass

class ObjectDetect:
 

    def object_detect_detail(self):
        return True#False


class Tesla(Battery,ObjectDetect):
    def __init__(self):
        pass 


    def stop(self):
        print("car is stop")
        self.is_stopped = True

    def move(self):
        

        if self.show_battery_percetage()  > 2:
            self.solar_charge()

            self.is_moving = True
            self.is_stopped = False
            if self.object_detect_detail() == True:
                self.stop()
                
        else:
            print(" Battery low")

        print("car is moving ")

    ######
    ######
    ######
        
tesla_obj = Tesla()
tesla_obj.move()

#condition
#loop
#list,dictionary
#function 

#class,inheritance




#student management system,calculator (class based)
  

