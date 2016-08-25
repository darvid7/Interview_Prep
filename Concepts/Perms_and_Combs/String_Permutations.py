"""
@author: David Lei
@since: 22/08/2016
@modified: 

Java coe
package Algo_Ds_Practice.Permutations;

/**
 * Created by David on 14/04/2016.
 * Time: 2:04 AM
 */

public class Permutations {


    public static void main(String[] args) {

        permuteStart("12");

    }

    public static void permuteStart ( String str ) {
        permute( str.toCharArray(), 0, str.length()-1 ); }

    public static void permute( char [] str, int low, int high ) {
        if ( low == high ) {
            String a = new String(str);
            System.out.println(a);
        }
        else {
            char tmp = str[ low ];
            for ( int i = low; i <= high; i++ ) {
                str[ low ] = str[ i ];
                str[ i ] = tmp;
                permute( str, low+1, high );
                str[ i ] = str[ low ];
            }
            str[ low ] = tmp; }
    }
}

"""