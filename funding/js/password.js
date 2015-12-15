/*비밀번호 일치 확인하는 js */


          var pass1 = document.getElementById('inputPassword');
          var pass2 = document.getElementById('inputPasswordTwice');
          var test = document.getElementById('test');
           pass1.onkeyup = function(event){

               event = event || window.event;
                if(pass1.value == null || pass1.value == ""){
                test.value ="";
                }else if(pass2.value == null || pass2.value == ""){
                test.value ="";
                }
               else if( pass2.value != pass1.value)
               {
                test.style.color="red";
                test.value ="비밀번호 불일치";
               }else if( pass2.value == pass1.value)
               {
               test.style.color="green";
                test.value = "비밀번호 일치";
               }
             }
               pass2.onkeyup = function(event){

               event = event || window.event;
                if(pass2.value == null || pass2.value == ""){
                test.value ="";
                }
               else if( pass2.value != pass1.value)
               {
                test.style.color="red";
                test.value ="비밀번호 불일치";
               }else if( pass2.value == pass1.value)
               {
               test.style.color="green";
                test.value = "비밀번호 일치";
               }
             }
              
