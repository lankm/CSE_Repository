/* Landon Moon
 * 1001906270
 * java 17.0.2
 * Windows 10 / Omega
 */

 import java.io.File;


public class lxm_lab01 {
  public static int dirSize(File dir) {
    int total = 0;

    // loop through files/directories
    for( File f: dir.listFiles() )
    {
      // if dir
      if(f.isDirectory())
        total += dirSize(f);
      // if file
      else
        total += f.length();
    }

    return total;
  }

  public static void main(String args[]) {
    // start at current dir
    int size = dirSize(new File("."));
    
    System.out.println(size);
  }
}
