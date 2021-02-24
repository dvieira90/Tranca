# Projeto Tranca

## <strong>Flash o firmware no node
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 <.bin>

## <strong>Cria alias no sistema para facilitar
alias node='ampy -b 115200 -p /dev/ttyUSB0 put main.py && ampy -b 115200 -p /dev/ttyUSB0 put funcs.py && minicom -b 115200 -D /dev/ttyUSB0'

## <strong>Copia arquivo para dentro do node
ampy -b 115200 -p /dev/ttyUSB0 put main.py

<button style='border-radius: 7px; padding: 10px; background-color: #1cbe70'>Teste</button>

<script>
    let bot = document.querySelect('button')
    bot.addEventListener('click', function (){
        bot.style.property.backgroundColor = '#3f51b' 
    })
</script>