var botui = new BotUI('prescreening');

botui.message
  .bot('Welcome to Akash-Vani. How can I help you today?')
  .then(function () {
    return botui.action.button({
      delay: 1000,
      action: [{
        text: 'Facing some problem',
        value: 'yes'
      }, {
        text: 'Book an appointment',
        value: 'no'
      }]
    })
}).then(function (res) {
  if(res.value == 'yes') {
    showReminderInput();
  } else {
    botui.message.bot('Okay.');
  }
});

var showReminderInput = function () {
  botui.message
    .bot({
      delay: 500,
      content: 'Please brief a bit about your problem:'
    })
    .then(function () {
      return botui.action.text({
        delay: 1000,
        action: {
          placeholder: 'Not feeling well'
        }
      })
    }).then(function (res) {
      botui.message
        .bot({
          delay: 500,
          content: 'Problem added: ' + res.value
        });

      return botui.action.button({
        delay: 1000,
        action: [{
          icon: 'plus',
          text: 'add another',
          value: 'yes'
        }]
      })
    }).then(showReminderInput);
}