$('.dropdown-toggle').dropdown();

moment.locale('ja', { week: { dow: 1 } });

var DateFormat = 'YYYY-MM-DD';
$(function () {
    $('#searchform-date').datetimepicker({
        inline: true,
        locale: moment.locale('ja'),
        format: DateFormat
    });

    $('#order-results').change(function() {
        var Url = window.location.href;
        console.log(this.value)
        switch(this.value){
            case "開始日(昇順）":
                var desc = "asc";
                break;
            case "開始日(降順)":
                var desc = "desc";
                break;
            default:
                var desc = "";
                break;
        }
        var regex = /\b(order_by=start_time-)[^&]*/;
        console.log(Url.match(regex));
        if(regex.test(Url)){
            var newUrl = Url.replace(regex, '$1' + desc);
        } else{
            var newUrl = Url + "&order_by=start_time-" + desc;
        }
        newUrl = newUrl.replace(/\bpage=\d+/,"page=1");
        window.location.replace(newUrl);
    });

    $('#result-number').change(function() {
        var Url = window.location.href;
        num = this.value
        var regex = /\b(numperpage=)[^&]*/;
        if(regex.test(Url)){
            var newUrl = Url.replace(regex, '$1' + num);
        } else{
            var newUrl = Url + "&numperpage=" + num;
        }
        window.location.replace(newUrl)
    });
});


/**
 * croppie-upload - use croppie.js to crop uploaded images
 */
(function (global) {
  var $ = global.jQuery;

  var base64ToBlob = function (src) {
    var chunkSize = 1024;

    var srcList = src.split(/[:;,]/);
    var mime = srcList[1];
    var byteChars = global.atob(srcList[3]);
    var byteArrays = [];

    for (var c = 0, len = byteChars.length; c < len; c += chunkSize) {
      var slice = byteChars.slice(c, c + chunkSize);
      var byteNumbers = new Array(slice.length);
      for (var i = 0; i < slice.length; i++) {
        byteNumbers[i] = slice.charCodeAt(i);
      }
      var byteArray = new Uint8Array(byteNumbers);
      byteArrays.push(byteArray);
    }

    return new Blob(byteArrays, {type: mime});
  };

  $.fn.extend({
    croppieUpload: function (opt) {
      var self = this;
      var div;

      // read file
      self.on('change', function () {
        $('.croppie-upload-ready').remove();

        div = $('<div>')
          .addClass('croppie-upload-ready')
          .croppie(
            $.extend({
              enableExif: true,
              viewport: {
                width: 200,
                height: 200,
                type: 'square'
              },
              boundary: {
                width: 300,
                height: 300
              }
            }, opt)
          );

        if (!this.files || !this.files[0]) {
          alert("Sorry - your browser doesn't support the FileReader API");
          return false;
        }

        var reader = new FileReader();
        reader.onload = function (e) {
          div.croppie('bind', {
            url: e.target.result
          });
        };
        reader.readAsDataURL(this.files[0]);
        self.after(div);
      });

      self.closest('form').submit(function () {
        var form = $(this);
        var formData = new FormData(form.get(0));
        var name = self.attr('name');

        div
          .croppie('result', {
            type: 'canvas',
            size: 'viewport'
          })
          .then(function (resp) {
            formData.set(name, base64ToBlob(resp), 'cropped');
            $.ajax({
              url: form.attr('action'),
              type: form.attr('method'),
              cache: false,
              processData: false,
              contentType: false,
              data: formData,
            })
            .done(function () {
              global.location.reload();
            });
          });

        return false;
      });
    }
  });
})(this);
