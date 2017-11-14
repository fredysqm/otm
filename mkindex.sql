ALTER TABLE `otm`.`mantenimiento_proveedor` ADD FULLTEXT INDEX `mantemiento_proveedor_fulltext` (`_searchtext` ASC);

DELIMITER //
CREATE PROCEDURE update_fts_index()
BEGIN
    UPDATE mantenimiento_proveedor SET _searchtext = CONCAT_WS(' ', id, razon_social, nro_documento);
END //
DELIMITER ;