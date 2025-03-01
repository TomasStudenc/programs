package filework;
import java.io.*;

import java.util.*;
import app.Aplikacia;


public class ReadfromFile {
    public static String readfromfile(String x, int pocet){
        try{
            if(x.equals("p")||x.equals("P")){
                BufferedReader br = new BufferedReader(new FileReader("skola_p.txt"));
                String line;
                if (pocet==0){
                    line=br.readLine();
                }else{
                    for(int i=0;i<pocet;i++){
                        br.readLine();
                    }
                    line=br.readLine();
                }
                br.close();
                return line;
                
            }
            else if(x.equals("t")||x.equals("T")){
            BufferedReader br = new BufferedReader(new FileReader("skola_t.txt"));
            String line;
            if (pocet==0){
                line=br.readLine();
            }else{
                for(int i=0;i<pocet;i++){
                    br.readLine();
                }
                line=br.readLine();
            }
            br.close();
            return line;
            
            }else{
                return "invalid input";
            }
            
        }
        catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            // Handle the exception appropriately, possibly return a default value
            return null;
        }


    }
    public static int readid(int id) {
        try {
            BufferedReader br = new BufferedReader(new FileReader("userID.txt"));
            String input;
            while ((input = br.readLine()) != null) {
                String[] parts = input.split("\\s+");
                if (parts.length > 0) {
                    int value = Integer.parseInt(parts[0]);
                    if (id == value) {
                        br.close();
                        return 0;
                    }
                }
            }
            br.close();
            return -1;
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return -1;
        }
    }
    public static String logsearch(String x){
        try {
            BufferedReader br = new BufferedReader(new FileReader("userID.txt"));
            String input;
            while ((input = br.readLine()) != null) {
                if (input.toLowerCase().contains(x)){
                    br.close();
                    return input;
                }
                }
                br.close();
                return "";
            
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return "";
        }

    }
    public static List<String> ziaklog(String search){
        List<String> matchingLines = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("userID.txt"));
            String line;

            while ((line = reader.readLine()) != null) {
                if (line.toLowerCase().contains(search)) {
                    matchingLines.add(line);
                }
            }

            reader.close();
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

        return matchingLines;
    }
    public static String list_all(String x,int pocet){
        try {
            if(x.equals("t")||x.equals("T")){
                BufferedReader br =  new BufferedReader(new InputStreamReader(new FileInputStream("list_skola_t.txt"), "UTF-8"));
                String line;
                if(pocet==0){
                    line=br.readLine();
                    br.close();
                    return line;
                }
                for(int i=0;i<pocet;i++){
                    br.readLine();
                }
                line=br.readLine();
                br.close();
                return line;
            }else if(x.equals("p")||x.equals("P")){
                BufferedReader br =new BufferedReader(new InputStreamReader(new FileInputStream("list_skola_p.txt"), "UTF-8"));
                String line;
                if(pocet==0){
                    line=br.readLine();
                    br.close();
                    return line;
                }
                for(int i=0;i<pocet;i++){
                    br.readLine();
                }
                line=br.readLine();
                br.close();
                return line;

            }else {
                return Aplikacia.error(3);
            }
        
            
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return Aplikacia.error(3);
        }
    }
}
