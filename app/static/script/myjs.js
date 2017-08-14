$(function(){
  var swiper = new Swiper('.swiper-container', {
    loop : true,
    pagination: '.swiper-pagination',
    nextButton: '.swiper-button-next',
    prevButton: '.swiper-button-prev',
    slidesPerView: 'auto',
    centeredSlides: true,
    paginationClickable: true,
    spaceBetween: 30
  });
  $('#top-tabs').tabs({
    selected  : 0,
  });
  var source   = $("#event-template").html();
  var template = Handlebars.compile(source);
  // var data = {
  //             "name": "ボランティア1",
  //             "date": "2017-08-08 00:00:00",
  //             "place": "北海道",
  //             "url":"/event/1",
  //             "status": "参加",
  //             "img":"/media/events/default_event_image.svg",
  // };
  var data ={
    "events": [
          {
              "id": 1,
              "name": "ボランティア1",
              "date": "2017-08-08 00:00:00",
              "place": "北海道",
              "status": "イベントステータス",
              "img":"/media/events/default_event_image.svg",
          },
          {
              "id": 2,
              "name": "ボランティア2",
              "date": "2017-08-08 00:00:00",
              "place": "北海道",
              "status": "イベントステータス",
              "img":"/media/events/default_event_image.svg",
          }
      ]
  };
  $('#event-area').html(template(data));
});

(function (window) {
  var $ = window.jQuery;
  var moment = window.moment;

  $('.dropdown-toggle').dropdown();

  $(function () {
    webshim.activeLang('ja');
    $.webshims.setOptions('extendNative', true);
    $.webshims.polyfill('forms');
  });

  moment.locale('ja', {week: {dow: 1}});

  var DateFormat = 'YYYY-MM-DD';
  $(function () {
    $('#searchform-date').datetimepicker({
      inline: true,
      locale: moment.locale('ja'),
      format: DateFormat
    });

    $('#order-results').change(function() {
      var Url = window.location.href;
      var desc;
      switch (this.value) {
        case "開始日(昇順）":
          desc = "asc";
          break;
        case "開始日(降順)":
          desc = "desc";
          break;
        default:
          desc = "";
          break;
      }
      var regex = /\b(order_by=start_time-)[^&]*/;
      var newUrl;
      if (regex.test(Url)) {
        newUrl = Url.replace(regex, '$1' + desc);
      } else {
        newUrl = Url + "&order_by=start_time-" + desc;
      }
      newUrl = newUrl.replace(/\bpage=\d+/, "page=1");
      window.location.replace(newUrl);
    });

    $('#result-number').change(function() {
      var Url = window.location.href;
      var num = this.value;
      var regex = /\b(numperpage=)[^&]*/;
      var newUrl;
      if (regex.test(Url)) {
        newUrl = Url.replace(regex, '$1' + num);
      } else {
        newUrl = Url + "&numperpage=" + num;
      }
      window.location.replace(newUrl);
    });
  });
})(this);

/**
 * bootstrap-confirmation2
 */
(function (global) {
  global.jQuery(function ($) {
    $('[data-toggle=confirmation]').confirmation({
      rootSelector: '[data-toggle=confirmation]',
      title: '本当によろしいですか？',
      btnOkLabel: 'はい',
      btnCancelLabel: 'いいえ'
    });
  });
})(this);

/**
 * croppie-upload - use croppie.js to crop uploaded images
 */
(function (global) {
  var $ = global.jQuery;
  var Blob = global.Blob;
  var alert = global.alert;
  var FileReader = global.FileReader;
  var FormData = global.FormData;

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
            formData.append(name, base64ToBlob(resp), 'cropped');
            $.ajax({
              cache: true,
              async: false,
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
