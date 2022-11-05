   let form = document.getElementById('form')

      form.addEventListener('submit', function(e){
       e.preventDefault()
       console.log('form submitted...')
   })
      document.getElementById('form-btn').addEventListener('click',function(e){

       submitFormData()

   })
    function submitFormData(){
        console.log('payment button clicked')

        let priceForm ={

            'price':form.price.value,

        }
        console.log(priceForm)


        let url ='/process/'
        fetch(url, {
            method: "POST",
            headers:{
                 'Content-Type':'application/json',
                 'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'form':priceForm })

        })
        .then((response) => response.json())
        .then((data) => {
          console.log('success:', data);
          alert('Done Checking payment');
          window.location.href = "{% url 'profile' %}";
        })
   }

