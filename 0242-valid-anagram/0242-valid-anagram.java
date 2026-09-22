import java.util.HashMap;
import java.util.HashMap;
import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String,String> map1=new HashMap<>();
        HashMap<String,String> map2=new HashMap<>();
        char[] arr1=s.toCharArray();
        Arrays.sort(arr1);
        char[] arr2=t.toCharArray();
        Arrays.sort(arr2);
        String sorted1=new String(arr1);
        String sorted2=new String(arr2);
        map1.put(s,sorted1);
        map2.put(t,sorted2);
        
        String val1=map1.get(s);
        String val2=map2.get(t);


        if (val1.equals(val2)){
            return true;
        }
        else{
            return false;
        }

        
    }
}