package filework;
import java.io.BufferedWriter;
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

import user.*;
import shool.Skola_p;
import shool.Skola_t;



public class WriteToFile {
  
  public static void writer_data(Ziak ziak) {
    try {
      
      
      BufferedWriter br = new BufferedWriter(new FileWriter("userID.txt",true));

      br.write(ziak.get_id()+" "+ziak.get_pp()+" "+ziak.get_dp()+" "+ziak.get_pt()+" "+ziak.get_dt()+"\n");
      
      br.close();
      System.out.println("");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }


  public static void fill_p_file(Skola_p[] p){
    try {
      FileWriter my_writer = new FileWriter("skola_p.txt");
      for(int i=0;i<101;i++){
        my_writer.write(i+": "+p[i].getCount()+" "+p[i].getPrv()+" "+p[i].getDruh()+"\n");
      }
      my_writer.close();
      System.out.println("");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }



  public static void fill_t_file(Skola_t[] t){
    try {
      FileWriter my_writer = new FileWriter("skola_t.txt");
      for(int i=0;i<101;i++){
        my_writer.write(i+": "+t[i].getCount()+" "+t[i].getPrv()+" "+t[i].getDruh()+"\n");
      }
      my_writer.close();
      System.out.println("");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }

}
