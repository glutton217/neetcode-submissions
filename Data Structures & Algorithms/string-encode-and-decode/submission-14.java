class Solution {

    public String encode(List<String> strs) {
        String encoded_string="";
        for (String word : strs){
            encoded_string+="#" + word.length() + "#" + word;
        }
        System.out.println(encoded_string);
        return encoded_string;
    }

    public List<String> decode(String str) {
        List<String> decoded_strs = new ArrayList<>();
        int strlen=str.length();
        String word="";
        int word_length=0;
        for(int i=0; i<strlen; i++){
            if(str.substring(i,i+1).equals("#") && word_length==0){
                word="";
                int digits=1;
                while(i+digits+1<strlen && str.substring(i+digits+1,i+2+digits).equals("#")==false){
                    digits++;
                }
                word_length=Integer.parseInt(str.substring(i+1,i+1+digits));
                System.out.println("word length: " + word_length);
                if(word_length==0){
                    decoded_strs.add("");
                }
                i+=digits+1;
                System.out.println(i);
            }
            else{
                word+=str.substring(i,i+1);
                word_length--;
                if(word_length==0){
                    decoded_strs.add(word);
                }
            }
        }
        return decoded_strs;
    }
}
