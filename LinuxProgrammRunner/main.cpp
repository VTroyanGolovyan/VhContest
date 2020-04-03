/* System calls libraries */
/* wait system calls */
#include <sys/wait.h>
/* we need rlimit system calls */
#include <sys/resource.h>
/* we need itimer call */
#include <sys/time.h>
/* we need fork system call */
#include <unistd.h>

#include <stdio.h>

void set_limits(int* n, char** args) {
  /* set memory limit */
  struct rlimit memory_limit;
  memory_limit.rlim_cur = 10000;
  memory_limit.rlim_max = 10000;
  setrlimit(RLIMIT_DATA, &memory_limit);
  /* set timelimit in seconds */
  struct rlimit time_limit;
  time_limit.rlim_cur = 1;
  time_limit.rlim_max = 1;
  setrlimit(RLIMIT_CPU, &time_limit);
  /* proccess limit */
  struct rlimit proccess_limit;
  proccess_limit.rlim_cur = 0;
  proccess_limit.rlim_max = 0;
  setrlimit(RLIMIT_NPROC, &proccess_limit);
}

void execute_programm(int* n, char** args) {
  printf("%s", "Hello, child");
}

int main(int n, char** args) {
  pid_t p_id = fork();
  if (p_id == 0) {
	set_limits(&n, args);
	freopen("input.txt", "a+",  stdin); //stdin file
	freopen("output.txt", "a+", stdout); //stdout file
	freopen("errors.txt", "a+", stderr); //stderr file
	execute_programm(&n, args);
  } else {
	 int wstatus;
	 struct rusage usage; 
     if (wait4(p_id, &wstatus, WUNTRACED | WCONTINUED, &usage) == p_id) {
		 printf("Memory usage: %ld\n", usage.ru_maxrss);
		 printf("CPU usage: %ld\n", usage.ru_stime.tv_usec);
     } else {
		 printf("%s", "Something went wrong");
	 }
  }
  return 0;
}
