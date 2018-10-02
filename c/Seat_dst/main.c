#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX_SEATS 5


struct seat_position{
  int      seat_no;
  double   x_position;
  double   y_position;
}seat[MAX_SEATS];

void input_seat_info(struct seat_position seat[])
{
  for (int i = 0; i < MAX_SEATS; i++)
  {
    memset(&seat[i], 0, sizeof(seat[i]));
    printf("Enter([seat no.] [x distance] [y distance] )>>");
    scanf("%d %lf %lf", &seat[i].seat_no, &seat[i].x_position, &seat[i].y_position);
  }
}
//Calculate distance between two seats.
void calc_seat_distance(struct seat_position seat[], double *max_distance, int *most_far_seat_no)
{
  double distance = 0.0, x_distance = 0.0, y_distance = 0.0;
  for(int i = 0; i < MAX_SEATS -1; i++)
  {
    for(int j = i +1; j < MAX_SEATS; j++)
    {
      x_distance = seat[i].x_position - seat[j].x_position;
      y_distance = seat[i].y_position - seat[j].y_position;
      distance   = sqrt(x_distance * x_distance + y_distance * y_distance);
      
      if(*max_distance < distance)
      {
        *max_distance = distance;
        most_far_seat_no[0] = seat[i].seat_no;
        most_far_seat_no[1] = seat[j].seat_no;
      }

    }
  }
}
int main(void)
{
  
  double max_distance = 0.0;
  int most_far_seat_no[2];

  //Input seat number, x position and y position.
  input_seat_info(seat);
  //Calculate distance between two seats.
  calc_seat_distance(seat, &max_distance, most_far_seat_no);
  //Display most far two seats and distance.
  printf("Most far seat: No.%d - No.%d, distance: %lf\n", most_far_seat_no[0], most_far_seat_no[1], max_distance);

}

