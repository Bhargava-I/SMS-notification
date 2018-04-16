<?php
require 'vendor/autoload.php';
use Plivo\RestClient;

$client = new RestClient('auth_id','auth_token');
$call_made = $client->calls->create(
    '12345678',
    ['441915740147'],
    'http://s3.amazonaws.com/static.plivo.com/answer.xml',
    'GET'
);
print_r($call_made);