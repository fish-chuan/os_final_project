#include <stdio.h>
#include <pthread.h>

#define MAX_SEQUENCE 100


int Fibo[MAX_SEQUENCE];
int num;


void *Fibonacci(int data){
    int i;
    int n= data;
    int a=0,b=1,c;
    //printf("i is %d\n",data);  

    for(i=0;i <=n;i++){
    	c=a+b;
    	a=b;
    	b=c;
    }
    Fibo[n+1]=c;
    //printf("real %d is %d\n",n,Fibo[n]); 
    
    
 }

void main(){
    pthread_t th[MAX_SEQUENCE];
    int data; 
    int ret; 
    int i=1;

    printf("The fibonacci produce programe!\nPlease input an number within 1~200: ");
    scanf("%d", &num);
    if(num < 0 || num > 100){
        printf("Your input is error.");
        return;
    }
	
    //create a thread
    for(i=0;i<num;i++){
    	ret = pthread_create(&th[i], NULL,Fibonacci,i);
    
    	if( ret != 0 ){
    	    printf("Create thread error!\n");
    	    return;
    	}
    }
    for(i=0;i<num;i++){
    	pthread_join(th[i], NULL);
    }
    
    if(num == 0){
        printf("Nothing output.");
    }
    else{
	for(i=0;i<=num;i++)
            printf("Fibo[%d]=%d \n",i,Fibo[i]);
        }
        printf("\n");
    
}
