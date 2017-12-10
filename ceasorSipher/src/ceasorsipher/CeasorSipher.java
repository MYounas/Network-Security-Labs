/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ceasorsipher;

import java.util.Scanner;

/**
 *
 * @author MY
 */
public class CeasorSipher {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner in=new Scanner(System.in);
        System.out.print("P.T:");
        String str=in.nextLine().toUpperCase();
        System.out.print("Key:");
        int key=in.nextInt();
        String str2=Encipher(str,key);
        System.out.println("Encipher :"+str2);
        System.out.println("Decipher :"+Decipher(str2,key));
        
    }
    
    static String Encipher(String str,int key){
        
        String str2="";
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i)==' ')
                str2+=' ';
            else{
                int a=( ( (int)(str.charAt(i)) - 64 + key)%26);
                if(a==0)
                    a=26;
                str2+=(char)(a + 64) ;
            }
        }
        
        return str2;
    }
    
    static String Decipher(String str,int key){
        
        String str2="";
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i)==' ')
                str2+=' ';
            else{
                int t=( (int)(str.charAt(i)) - 64 - key);
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
