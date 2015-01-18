

var handler = StripeCheckout.configure({
  key: '{{stripe_key}}',
  image: '{{album.cover_art.url}}',
  token: function(token) {
      $.ajax({
        type: "POST",
        url: '/charge/',
        data:  {'stoken':token.id, 
                'email':token.email,
                'csrfmiddlewaretoken': '{{ csrf_token }}',
                'album':{{album.pk}}
              },
      }).done(function(response) { 
        window.location.href = response.redirecturl;
      });
  }
});

document.getElementById('pay-button').addEventListener('click', function(e) {
  // Open Checkout with further options
  handler.open({
    name: '{{album.name}}',
    description: '{{album.name}} Digital Download',
    amount: {% if album.price_incents %}{{album.price_incents}}{% else %}0{% endif %}
  });
  e.preventDefault();
});