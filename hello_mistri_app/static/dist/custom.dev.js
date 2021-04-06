"use strict";

$(document).ready(function () {
  $('#ClintAccount').hide();
  $('#MistriAccount').hide();
  $('#ClintAccountBTN').click(function () {
    $('#ClintAccount').show(1000);
    $('#MistriAccount').hide(1000);
  });
  $('#MistriAccountBTN').click(function () {
    $('#ClintAccount').hide(1000);
    $('#MistriAccount').show(1000);
  });
});