/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hillcipher;

//import com.sun.org.apache.bcel.internal.generic.AALOAD;
import java.util.Scanner;

/**
 *
 * @author MY
 */
public class HillCipher {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Scanner in =new Scanner(System.in);
        
//        always without space
        String PT=in.nextLine().toUpperCase();
        int key[][]={
            {3,3},
            {2,5}
        };
        int txtMat[][]=new int[2][1];
        String ecText="";
        
        for (int i = 0; i < PT.length(); ) {
            txtMat[0][0]=(int)(PT.charAt(i++))-64;
            txtMat[1][0]=(int)(PT.charAt(i++))-64;
            txtMat=afterCalMat(txtMat,key);
            ecText+= (char)(txtMat[0][0]%26+64);
            ecText+= (char)(txtMat[1][0]%26+64);
        }
        
        System.out.println(ecText);
        
    }

    private static int[][] afterCalMat(int[][] txtMat, int[][] key) {
        
        int tempMat[][]=new int[2][1];
        
        for (int i = 0; i < 2; i++) {
            tempMat[i][0]=0;
            for (int j = 0; j < 2; j++) {
                tempMat[i][0]+=key[i][j]*txtMat[j][0];
            }
        }
        return tempMat;
    }
    
}
