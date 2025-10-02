//유효성체크
$("input[name='hour']").on("input", function () {
        let value = $(this).val();
        value = value.replace(/[^0-9.]/g, '') //숫자와 소수점만 허용
        value = value.replace(/(\.)(\.)+/g, '$1'); //소수점이 여러개 들어오면 첫번째만 유지
        $(this).val(value);
    });