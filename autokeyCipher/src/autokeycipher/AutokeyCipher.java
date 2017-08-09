/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package autokeycipher;

import java.util.Scanner;

/**
 *
 * @author MY
 */
public class AutokeyCipher {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner in=new Scanner(System.in);
        String str=in.nextLine().toUpperCase();
        String str2="";
        String key="MATH";
        for (int i = 0,j=0; i < str.length(); i++) {
            if(str.charAt(i)==' '){
                str2+=" ";
                continue;
            }
            
            if(j==key.length()){
                j=0;
                key=str;
            }
            
            if(key.charAt(j)==' ')
                j++;
            str2+=key.charAt(j++);
        }
        
        String str3=Encipher(str,str2);
        System.out.println("Encipher :"+str2);
        System.out.println("Decipher :"+Decipher(str3,str2));
        
    }
 
    
     static String Encipher(String str,String key){
        
        String str2="";
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i)==' ')
                str2+=' ';
            else{
                int a=( (int)(str.charAt(i)) - 64) + ( (int)(key.charAt(i)) - 64);
                int b=a % 26;
                if(b==0)
                    b=26;
                str2+=(char)( b +64) ;
            }
        }
        
        return str2;
    }
    
    static String Decipher(String str,String key){
        
        String str2="";
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i)==' ')
                str2+=' ';
            else{
                int t=( (int)(str.charAt(i)) - 64) - ( (int)(key.charAt(i)) - 64);
                if(t<=0)
                    t+=26;
                int t1=(t %26);
                if(t1==0)
                    t1=26;
                str2+=(char)(t1 +64) ;
            }
        }
        
        return str2;
    }
}
