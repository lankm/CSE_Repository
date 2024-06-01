/* Landon Moon
 * 1001906270
 * gcc 10.3.0
 * Windows 10 / Omega
 * 
 * Here is my little rant about how c on linux requires a / for
 * the file system and not a \ even though its displayed with \.
 * took me like an hour to figure out why omega couldn't find the files
 */

//#include <errno.h>

#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define BUFSIZE 128

int dirSize(const char *path)
{
  int size = 0;

  char newPath[BUFSIZE];
  strcpy(newPath, path);
  
  /* opening directory */
  DIR *d = opendir(path);
  
  /* error checking */
  if(d==0)
    return size;

  /* loop through all files */
  struct dirent *de;
  while(de = readdir(d))
  {
    /* skip . and .. */
    if (!strcmp(de->d_name, ".") || !strcmp(de->d_name, ".."))
    {
      continue;
    }

    /* making newpath */
    strcat(newPath, "/");
    strcat(newPath, de->d_name);

    /* get information on file */
    struct stat properties;
    stat(newPath, &properties);
    
    //printf("%s ", strerror(errno));
    //printf("%s\n", newPath);

    /* if subdirectory */
    if( S_ISDIR(properties.st_mode) )
    {
      /* recur and add subtotal */
      size += dirSize(newPath);
    }
    /* if file */
    else if( S_ISREG(properties.st_mode))
    {
      /* add size of file */
      FILE *fp = fopen(newPath, "r");
      fseek(fp, 0L, SEEK_END);
      size += ftell(fp);
    }

    /* reset buffer for next file */
    strncpy(newPath, path, BUFSIZE);
  }

  return size;
}

int main(int argc, const char* argv[])
{
  /* start in current directory */
  int size = dirSize(".");
  printf("%d\n", size);

  return 0;
}
