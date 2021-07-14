const mascaraCNPJ = id => {
    let cnpj = ''
    cnpj = document.getElementById(id).value
    cnpj = cnpj.replace(/\D/g, "")
    cnpj = cnpj.replace(/^(\d{2})(\d)/, "$1.$2")
    cnpj = cnpj.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
    cnpj = cnpj.replace(/\.(\d{3})(\d)/, ".$1/$2")
    cnpj = cnpj.replace(/(\d{4})(\d)/, "$1-$2")
    document.getElementById(id).value = cnpj
}

const mascaraTelefone = id => {
    let telefone = ''
    telefone = document.getElementById(id).value
    telefone = telefone.replace(/^(\d{2})(\d)/, "($1) $2" )
    document.getElementById(id).value = telefone
}