ALTER TABLE core_proveedor ADD FULLTEXT INDEX core_proveedor_fts (`_fts` ASC);

DELIMITER //
CREATE PROCEDURE update_fts_index()
BEGIN
    UPDATE core_proveedor SET _fts = CONCAT_WS(' ', id, razon_social, nro_documento);
END //
DELIMITER ;