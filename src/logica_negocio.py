
def calcular_descuento(subtotal_bruto: float, tipo_cliente: str) -> float:
    """Calcula el monto de descuento según el tipo de cliente y el subtotal."""
    tipo_cliente = tipo_cliente.upper().strip()
    porcentaje_vip_alto = 0.15
    porcentaje_vip_bajo = 0.10
    porcentaje_reg_alto = 0.08
    porcentaje_reg_bajo = 0.03

    if tipo_cliente == "VIP":
        if subtotal_bruto > 500.0:
            return subtotal_bruto * porcentaje_vip_alto
        return subtotal_bruto * porcentaje_vip_bajo

    if tipo_cliente == "REGULAR":
        if subtotal_bruto > 500.0:
            return subtotal_bruto * porcentaje_reg_alto
        return subtotal_bruto * porcentaje_reg_bajo

    return 0.0


def procesar_factura(subtotal_bruto: float, tipo_cliente: str) -> dict:
    """Integra los cálculos de descuento, IGV y total a pagar."""
    tasa_igv = 0.18

    monto_descuento = calcular_descuento(subtotal_bruto, tipo_cliente)
    subtotal_con_descuento = subtotal_bruto - monto_descuento
    monto_igv = subtotal_con_descuento * tasa_igv
    total_a_pagar = subtotal_con_descuento + monto_igv

    return {
        "subtotal_bruto": round(subtotal_bruto, 2),
        "descuento": round(monto_descuento, 2),
        "subtotal_neto": round(subtotal_con_descuento, 2),
        "igv": round(monto_igv, 2),
        "total_pagar": round(total_a_pagar, 2),
    }


def validar_numero_positivo(entrada_texto: str) -> bool:
    """Valida si el texto ingresado es un número decimal positivo válido."""
    try:
        numero = float(entrada_texto.strip())
        return numero > 0 and numero != float("inf") and numero == numero
    except (ValueError, OverflowError):
        return False
