from commonconf import override_settings

FGRAD = 'restclients.dao_implementation.grad.File'
fdao_grad_override = override_settings(RESTCLIENTS_GRAD_DAO_CLASS=FGRAD)
