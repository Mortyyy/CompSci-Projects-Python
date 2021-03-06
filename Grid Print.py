#Author: Alex
#Date: 3/18/15

print""
print"-----------Boolean Function with Modulo-----------"

def  is_divisible(x, y):
    if(x % y == 0):
        return True
        print"True"
    else:
        return False
        print"False"
	
is_divisible(6, 4)
is_divisible(6, 3)

print"----------Boolean Function for Divisibility-----------"

def test_divisible(x,y):
    print""
    print"If x is",x,"and y is",y,"then:"
    if is_divisible(x,y):
        print 'x is divisible by y'
    else:
        print 'x is NOT divisible by y'

test_divisible(6,4)
test_divisible(6,3)

rt 1        rightMotor          393 Motor             Right side motor
Motor Port 10       leftMotor           393 Motor             Left side motor, Reversed
I2C_1               rightIEM            Integrated Encoder    Encoder mounted on rightMotor
I2C_2               leftIEM             Integrated Encoder    Encoted mounted on leftMotor
----------------------------------------------------------------------------------------------------*/

//NOTE: 627 ticks is one full wheel rotation.
//			Half power is 63.

//Clear the encoders associated with the left and right motors
void resetEncoder(){
	nMotorEncoder[rightIEM] = 0;
	nMotorEncoder[leftIEM] = 0;
}

//Stops robot.
void stopRobot(){
	motor[rightMotor] = 0;
	motor[leftMotor]	= 0;
}

task main
{
	wait1Msec(2000);
	resetEncoder();
	stopRobot();

	//While less than 1000 encoder counts of the right motor
 	while(SensorValue[leftIEM] < 400)
	{
		//Move forward at half power
		motor[rightMotor] = 30;
		motor[leftMotor]	= 30;
	}

	  motor[rightMotor] = 0;
		motor[leftMotor]	= 0;
		wait1Msec(1000);

	resetEncoder();

	//While less than 1000 encoder counts of the right motor
 	while(SensorValue[leftIEM] > -400)
	{
		//Move in reverse at half power
		motor[rightMotor] = -30;
		motor[leftMotor]	= -30;
	}
}
