   let form = document.getElementById('form')

      form.addEventListener('submit', function(e){
       e.preventDefault()
       console.log('form submitted...')
   })
      document.getElementById('form-btn').addEventListener('click',function(e){

       submitFormData()

   })
    function submitFormData(){
        let massage = document.getElementById('massage')

        console.log('payment button clicked')

        let withdrawerForm ={

            'wallet':form.wallet.value,
            'walletAddress':form.walletAddress.value,
            'amount':form.amount.value,

        }
        console.log(withdrawerForm)


        let url ='/withdrawer/'
        fetch(url, {
            method: "POST",
            headers:{
                 'Content-Type':'application/json',
                 'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'form':withdrawerForm })

        })
        .then((response) => response.json())
        .then((data) => {
          console.log('success:', data);
           massage.innerHTML = data.massage
        })
   }

